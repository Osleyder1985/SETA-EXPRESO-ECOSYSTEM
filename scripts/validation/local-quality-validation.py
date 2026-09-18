#!/usr/bin/env python3
"""Local, zero-cost reproduction of the repository Quality Validation contract.

This validator intentionally mirrors QV-001..QV-006 from
.github/workflows/quality-validation.yml. It does not replace the authoritative
GitHub workflow; it reduces unnecessary Actions executions by detecting the
same classes of defects before pushing.
"""
from pathlib import Path
import re
import sys

ROOT = Path(".").resolve()
EXCLUDED = {".git"}
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

REQUIRED = [
    "README.md",
    "docs/Governance/00-Software-Lifecycle-Master.md",
    "docs/Governance/03-Artifacts-And-Evidence.md",
    "docs/Governance/04-Quality-Gates.md",
    "docs/Governance/05-Repository-Naming-Convention.md",
    "docs/Governance/06-Change-Control-Workflow.md",
    "docs/Governance/07-Main-Protection-Strategy.md",
    "docs/Governance/08-Software-Roadmap.md",
    "docs/Governance/09-Issue-And-Pull-Request-Labeling-Policy.md",
    "docs/Governance/10-Governance-Enforcement-Architecture.md",
    "docs/Governance/11-Governance-Control-Matrix.md",
    "docs/Governance/12-Quality-Validation-Architecture.md",
    "docs/Governance/13-Security-Validation-Architecture.md",
    "docs/Governance/14-Evidence-Validation-Architecture.md",
    "docs/Governance/17-Risk-Management-System.md",
    "docs/Governance/18-Risk-Management-Control-Matrix.md",
    "docs/Governance/19-Decision-Governance.md",
    "docs/Governance/20-Decision-Governance-Control-Matrix.md",
    "docs/Governance/21-Engineering-Metrics-Governance.md",
    "docs/Governance/22-Engineering-Metrics-Control-Matrix.md",
    "docs/Governance/Metrics/Metric-Catalog.yml",
    "docs/Governance/Metrics/Engineering-Governance-Dashboard.md",
    "docs/Governance/Metrics/Engineering-Governance-Dashboard.html",
    ".github/workflows/governance-validation.yml",
    ".github/workflows/quality-validation.yml",
    ".github/workflows/security-validation.yml",
    ".github/workflows/evidence-validation.yml",
]

def files_matching(patterns):
    result = []
    for pattern in patterns:
        result.extend(ROOT.glob(pattern))
    return sorted({p for p in result if ".git" not in p.parts})

def fail(code, message):
    print(f"FAIL {code}: {message}")
    return False

ok = True

# QV-001 / QV-002
md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
if not md_files:
    ok = fail("QV-001", "no hay archivos Markdown para validar.")
else:
    for p in md_files:
        if not p.stat().st_size:
            ok = fail("QV-001", f"archivo Markdown vacío: {p.relative_to(ROOT)}") and ok
            continue
        first = p.read_text(encoding="utf-8").splitlines()[0] if p.read_text(encoding="utf-8").splitlines() else ""
        if not re.match(r"^# .+", first):
            ok = fail("QV-002", f"el Markdown debe comenzar con H1: {p.relative_to(ROOT)}") and ok
if ok:
    print("PASS QV-001/QV-002: Markdown no vacío y con H1.")

# QV-003
non_md = [
    p for p in ROOT.rglob("*")
    if p.is_file() and ".git" not in p.parts
    and p.suffix.lower() not in {".md", ".png", ".jpg", ".jpeg", ".gif"}
]
for p in non_md:
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    for n, line in enumerate(text.splitlines(), 1):
        if re.search(r"[ \t]$", line):
            ok = fail("QV-003", f"trailing whitespace: {p.relative_to(ROOT)}:{n}") and ok
if ok:
    print("PASS QV-003: no se detectó trailing whitespace.")

# QV-004: prefer Ruby if available, otherwise PyYAML.
yaml_files = sorted({p for ext in ("*.yml", "*.yaml") for p in ROOT.rglob(ext) if ".git" not in p.parts})
if not yaml_files:
    ok = fail("QV-004", "no hay archivos YAML para validar.") and ok
else:
    try:
        import yaml  # type: ignore
    except ImportError:
        yaml = None
    if yaml is None:
        print("WARN QV-004: PyYAML no está instalado; instalarlo para validar YAML localmente.")
        ok = False
    else:
        for p in yaml_files:
            try:
                yaml.safe_load(p.read_text(encoding="utf-8"))
            except Exception as exc:
                ok = fail("QV-004", f"{p.relative_to(ROOT)}: {exc}") and ok
if ok:
    print(f"PASS QV-004: {len(yaml_files)} archivos YAML procesados.")

# QV-005
for document in md_files:
    text = document.read_text(encoding="utf-8")
    for target in MARKDOWN_LINK.findall(text):
        target = target.strip().split()[0]
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        candidate = (document.parent / target_path).resolve()
        if not candidate.exists():
            ok = fail("QV-005", f"{document.relative_to(ROOT)}: enlace local inexistente: {target}") and ok
if ok:
    print("PASS QV-005: no se detectaron enlaces locales Markdown rotos.")

# QV-006
for rel in REQUIRED:
    p = ROOT / rel
    if not p.is_file() or not p.stat().st_size:
        ok = fail("QV-006", f"artefacto crítico ausente o vacío: {rel}") and ok
if ok:
    print("PASS QV-006: artefactos críticos presentes y no vacíos.")

print("QUALITY_VALIDATION_LOCAL=" + ("PASS" if ok else "FAIL"))
sys.exit(0 if ok else 1)
