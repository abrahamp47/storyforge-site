#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


class InternalLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        attr_map = {k: v for k, v in attrs}
        href = attr_map.get("href")
        cls = attr_map.get("class", "")
        if href and "internal" in cls:
            self.hrefs.append(href)


def target_exists(site_root: Path, html_file: Path, href: str) -> bool:
    href = href.split("#", 1)[0]
    if not href or href.startswith("http"):
        return True
    if href.startswith("/"):
        target = (site_root / href.lstrip("/")).resolve()
    else:
        target = (html_file.parent / href).resolve()
    candidates = [target] if target.suffix == ".html" else [Path(str(target) + ".html"), target / "index.html"]
    return any(c.exists() for c in candidates)


def main() -> int:
    root = Path(__file__).resolve().parents[1] / "public"
    broken: list[tuple[str, str]] = []
    for html in root.rglob("*.html"):
        parser = InternalLinkParser()
        parser.feed(html.read_text(encoding="utf-8", errors="ignore"))
        for href in parser.hrefs:
            if not target_exists(root, html, href):
                broken.append((html.relative_to(root).as_posix(), href))

    print(f"broken {len(broken)}")
    for src, href in broken[:400]:
        print(f"{src} -> {href}")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
