#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md", "ARTICLE.md", "SUPPLEMENTAL_FINDINGS.md",
    "PUBLIC_EXPORT_MANIFEST.md", "PROVENANCE.md", "LICENSE.md", "CITATION.cff",
    "methodology/METHODOLOGY.md", "methodology/CLAIMS_AND_LIMITATIONS.md",
    "methodology/REPRODUCIBILITY.md", "methodology/HARDWARE.md",
    "results/INDEX.md", "results/quantization/GSM8K_IFEVAL.md",
    "results/quantization/gsm8k_ifeval.json",
    "results/context/LONG_CONTEXT.md", "results/context/long_context.json",
    "results/serving/RTX5090_STACKS.md", "results/serving/rtx5090_stacks.json",
    "results/serving/LLAMACPP_Q4.md", "results/serving/llamacpp_q4.json",
    "results/reasoning/TEMPLATE_SEMANTICS.md", "results/reasoning/template_semantics.json",
    "results/reasoning/HARD_PACK.md", "results/reasoning/hard_pack.json",
    "results/reasoning/SHADER_BUDGET.md", "results/reasoning/shader_budget.json",
    "results/reasoning/VERBOSITY.md", "results/reasoning/verbosity.json",
    "results/reasoning/TEMPERATURE.md", "results/reasoning/temperature.json",
    "results/coding/CODING.md", "results/coding/coding_status.json",
    "results/harness/RECOVERY_AND_INVALID_RUNS.md", "results/holds/PROTOCOL_HOLDS.md",
    "supplemental/PROGRAMBENCH_Q11A.md", "supplemental/programbench_q11a_reasoning.json",
    "supplemental/AEON_PUBLIC_SAFE.md", "data/master_results.csv",
    "figures/fig-5090-stacks.svg", "figures/fig-hardpack.svg", "figures/fig-shader.svg",
    "figures/fig-verbosity.svg", "figures/fig-quant.svg", "figures/fig-preserve.svg",
    "figures/fig-context.svg", "figures/fig-llamacpp.svg", "figures/fig-programbench-q11a.svg",
]

TEXT_SUFFIXES = {".md", ".json", ".csv", ".yml", ".yaml", ".py", ".cff", ".svg"}
SECRET_PATTERNS = {
    "github token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-like key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "HuggingFace token": re.compile(r"\bhf_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Linux home path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "Windows user path": re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\\\\s]+"),
}
FORBIDDEN_INTERNAL = [
    "CURRENT_CAMPAIGN_STATE", "RECOVERY_READ_ORDER", "PROTECTED_HARDWARE",
    "CURRENT_SESSION_ID", "raw_private/", "GPU1/:8028",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def text_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and ".git" not in p.parts and p.suffix.lower() in TEXT_SUFFIXES:
            yield p


# Required surface
missing = [p for p in REQUIRED if not (ROOT / p).is_file()]
if missing:
    fail("missing required files: " + ", ".join(missing))

# JSON validity
for p in ROOT.rglob("*.json"):
    if ".git" in p.parts:
        continue
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"invalid JSON {p.relative_to(ROOT)}: {e}")

# Secrets / local paths / operational internals
for p in text_files():
    if p.relative_to(ROOT).as_posix() == "tools/verify_public_release.py":
        continue
    text = p.read_text(encoding="utf-8", errors="replace")
    for label, rx in SECRET_PATTERNS.items():
        if rx.search(text):
            fail(f"{label} pattern in {p.relative_to(ROOT)}")
    for marker in FORBIDDEN_INTERNAL:
        if marker in text:
            fail(f"internal marker {marker!r} in {p.relative_to(ROOT)}")

# Relative markdown/image links
link_rx = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
for p in ROOT.rglob("*.md"):
    text = p.read_text(encoding="utf-8", errors="replace")
    for target in link_rx.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (p.parent / target).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            fail(f"link escapes repo in {p.relative_to(ROOT)}: {target}")
        if not resolved.exists():
            fail(f"broken relative link in {p.relative_to(ROOT)}: {target}")

# Headline claim traces
checks = [
    ("151.27", ["README.md", "ARTICLE.md", "results/serving/RTX5090_STACKS.md", "results/serving/rtx5090_stacks.json", "data/master_results.csv"]),
    ("42624", ["results/context/long_context.json", "results/serving/rtx5090_stacks.json"]),
    ("42,624", ["README.md", "ARTICLE.md", "results/context/LONG_CONTEXT.md", "results/holds/PROTOCOL_HOLDS.md"]),
    ("308/502", ["README.md", "ARTICLE.md", "supplemental/PROGRAMBENCH_Q11A.md"]),
    ("61.35", ["supplemental/programbench_q11a_reasoning.json", "data/master_results.csv"]),
]
for needle, files in checks:
    for rel in files:
        text = (ROOT / rel).read_text(encoding="utf-8", errors="replace")
        if needle not in text:
            fail(f"claim trace {needle!r} missing from {rel}")

print(f"PUBLIC RELEASE VALIDATION PASS ({len(REQUIRED)} required files)")
