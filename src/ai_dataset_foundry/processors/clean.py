from __future__ import annotations

import re

_REPEATED_LINE = re.compile(r"^(.*)\n(?:\1\n){2,}", re.MULTILINE)


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = "".join(ch for ch in text if ch in "\n\t" or ord(ch) >= 32)
    text = _REPEATED_LINE.sub(r"\1\n", text)
    return text.strip()
