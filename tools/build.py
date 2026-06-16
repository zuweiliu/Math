#!/usr/bin/env python3
"""
build.py — render lesson spec files into standalone HTML pages.

Each lesson lives in its own folder under `lessons/` (e.g. `lessons/lesson-19/`)
holding the spec plus any source material (PDF, notes, generated HTML). A lesson
spec is a Python file in that folder that builds a `lessonkit.Lesson` and exposes
it as a module-level variable named `lesson`. It may also define
`OUTPUT = "Lesson 19 - Title.html"` to choose the output filename (default: the
spec's own name with a .html extension).

Usage:
    python3 tools/build.py lessons/lesson-19/lesson19.py   # build one
    python3 tools/build.py --all                            # build every lessons/**/*.py
    python3 tools/build.py lessons/lesson-19/lesson19.py --out "Lesson 19.html"

Output HTML is written into the spec's own folder. The links to
`common/lesson.css` / `common/lesson.js` are resolved with a relative asset
prefix that is computed automatically from the output location.
"""
from __future__ import annotations
import argparse
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # workspace root
LESSONS_DIR = os.path.join(ROOT, "lessons")
sys.path.insert(0, os.path.join(ROOT, "tools"))


def _load(spec_path: str):
    spec_path = os.path.abspath(spec_path)
    name = os.path.splitext(os.path.basename(spec_path))[0]
    spec = importlib.util.spec_from_file_location(name, spec_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot import {spec_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod, name


def _assets_prefix(out_path: str) -> str:
    rel = os.path.relpath(ROOT, os.path.dirname(os.path.abspath(out_path)))
    return "" if rel == "." else rel.replace(os.sep, "/") + "/"


def build_one(spec_path: str, out: str | None = None) -> str:
    mod, name = _load(spec_path)
    if not hasattr(mod, "lesson"):
        raise SystemExit(f"{spec_path}: must define a module-level `lesson` variable")
    out_name = out or getattr(mod, "OUTPUT", None) or f"{name}.html"
    spec_dir = os.path.dirname(os.path.abspath(spec_path))
    out_path = out_name if os.path.isabs(out_name) else os.path.join(spec_dir, out_name)
    html = mod.lesson.render(assets_prefix=_assets_prefix(out_path))
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✓ {os.path.relpath(spec_path, ROOT)}  →  {os.path.relpath(out_path, ROOT)}")
    return out_path


def _find_specs() -> list[str]:
    """Every lessons/**/*.py spec (skipping files starting with '_')."""
    found: list[str] = []
    for dirpath, _dirs, files in os.walk(LESSONS_DIR):
        for f in files:
            if f.endswith(".py") and not f.startswith("_"):
                found.append(os.path.join(dirpath, f))
    return sorted(found)


def main() -> None:
    ap = argparse.ArgumentParser(description="Render lesson specs to HTML.")
    ap.add_argument("spec", nargs="?", help="path to a lessons/<name>/*.py spec")
    ap.add_argument("--all", action="store_true", help="build every lessons/**/*.py")
    ap.add_argument("--out", help="output HTML path (single build only)")
    args = ap.parse_args()

    if args.all:
        specs = _find_specs()
        if not specs:
            raise SystemExit("no lesson specs found under lessons/")
        for s in specs:
            build_one(s)
    elif args.spec:
        build_one(args.spec, args.out)
    else:
        ap.print_help()
        raise SystemExit(1)


if __name__ == "__main__":
    main()
