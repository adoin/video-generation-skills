#!/usr/bin/env python3
"""Scan Scrapling tutorials_md and build tutorial → skill mapping.

Usage:
  python scripts/build-index.py --source ../Scrapling/output/tutorials_md
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SKILL_RULES: list[tuple[str, list[str]]] = [
    ("prompt-director", [r"提示词创作", r"提示词分享", r"【设计教程】"]),
    ("ecommerce", [r"电商", r"服装出海", r"保健品", r"Urdru", r"Uncolive", r"富吃虾条"]),
    ("brand-ad-cg", [r"品牌提升", r"品牌美学", r"品牌升级", r"品牌CG", r"品牌工作流", r"TVC", r"商业广告", r"企业宣传", r"创意视频", r"创意美学", r"创意玩法", r"创新玩法"]),
    ("ai-video-director", [r"AI短剧", r"AI漫剧", r"3D漫剧", r"AI影视", r"AI短片", r"影视制作", r"【AI视频】", r"【AI技巧】"]),
]


def classify(filename: str) -> list[str]:
    matched = []
    for skill, patterns in SKILL_RULES:
        if any(re.search(p, filename) for p in patterns):
            matched.append(skill)
    return matched or ["unclassified"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("sources/tutorial-index-full.json"))
    args = parser.parse_args()

    entries = []
    for md in sorted(args.source.glob("*.md")):
        skills = classify(md.name)
        entries.append({"file": md.name, "skills": skills})

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(entries)} entries to {args.out}")


if __name__ == "__main__":
    main()
