"""Render complete language pages from the Chinese HTML and translation dictionaries.

Run python3 scripts/build-locales.py after editing index.html or locales/*.json.
Only uses the Python standard library; generated pages are committed and deployed.
"""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://jetbrains-keygen.kkplayit.online/"
LOCALES = {"en": "en_US", "ko": "ko_KR", "ru": "ru_RU"}
VOID = set("area base br col embed hr img input link meta param source track wbr".split())


class Translate(HTMLParser):
    def __init__(self, source, messages, locale):
        super().__init__(convert_charrefs=False)
        self.source, self.messages, self.locale = source, messages, locale
        self.lines = [0]
        for line in source.splitlines(keepends=True):
            self.lines.append(self.lines[-1] + len(line))
        self.stack, self.edits = [], []

    def source_offset(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        start = self.source_offset()
        raw = self.get_starttag_text()
        changed = False
        for marker, attr in (("data-i18n-ph", "placeholder"), ("data-i18n-aria", "aria-label")):
            if marker in attrs:
                attrs[attr] = self.messages[attrs[marker]]
                changed = True
        if tag == "html":
            attrs["lang"] = self.locale
            changed = True
        if tag == "a" and attrs.get("hreflang"):
            attrs.pop("aria-current", None)
            if attrs["hreflang"] == self.locale:
                attrs["aria-current"] = "page"
            changed = True
        if tag == "link" and attrs.get("rel") == "canonical":
            attrs["href"] = BASE + self.locale + "/"
            changed = True
        if tag == "meta":
            key = attrs.get("name", attrs.get("property"))
            values = {
                "description": self.messages["metaDescription"],
                "og:title": self.messages["docTitle"],
                "twitter:title": self.messages["docTitle"],
                "og:description": self.messages["metaDescription"],
                "twitter:description": self.messages["metaDescription"],
                "og:site_name": self.messages["siteName"],
                "og:url": BASE + self.locale + "/",
                "og:locale": LOCALES[self.locale],
            }
            if key in values:
                attrs["content"] = values[key]
                changed = True
        if changed:
            rendered = "<" + tag + "".join(
                " " + k if v is None else f' {k}="{escape(v, quote=True)}"'
                for k, v in attrs.items()
            ) + ">"
            self.edits.append((start, start + len(raw), rendered))
        if tag not in VOID:
            self.stack.append((tag, start + len(raw), attrs))

    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1][0] == tag, f"Unbalanced HTML: {tag}"
        _, start, attrs = self.stack.pop()
        end = self.source_offset()
        for marker in ("data-i18n", "data-i18n-html", "data-i18n-code"):
            if marker in attrs:
                value = self.messages[attrs[marker]]
                if marker != "data-i18n-html":
                    value = escape(value, quote=False)
                self.edits.append((start, end, value))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            data = json.loads(self.source[start:end])
            data.update(name=self.messages["siteName"], url=BASE + self.locale + "/",
                        inLanguage=self.locale, description=self.messages["metaDescription"])
            self.edits.append((start, end, "\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n"))

    def render(self):
        self.feed(self.source)
        assert not self.stack, "Unclosed HTML tags"
        result = self.source
        boundary = len(result)
        for start, end, replacement in sorted(self.edits, reverse=True):
            assert end <= boundary, "Overlapping translations: avoid nested translation markers"
            result = result[:start] + replacement + result[end:]
            boundary = start
        return result


def build():
    source = (ROOT / "index.html").read_text()
    keys = set(re.findall(r'data-i18n(?:-html|-code|-ph|-aria)?="([^"]+)"', source))
    for locale in LOCALES:
        messages = json.loads((ROOT / "locales" / f"{locale}.json").read_text())
        assert keys <= messages.keys(), f"Missing {locale} translations: {keys - messages.keys()}"
        result = Translate(source, messages, locale).render()
        (ROOT / locale).mkdir(exist_ok=True)
        (ROOT / locale / "index.html").write_text(result)
        print(f"Built /{locale}/ ({len(keys)} translation keys)")

    urls = [BASE] + [BASE + locale + "/" for locale in LOCALES]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sitemap += "".join(f"  <url><loc>{url}</loc></url>\n" for url in urls)
    (ROOT / "sitemap.xml").write_text(sitemap + "</urlset>\n")


if __name__ == "__main__":
    build()
