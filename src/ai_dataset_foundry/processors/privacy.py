from __future__ import annotations

import re

_SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*[\"']?[A-Za-z0-9_\-./+=]{12,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

_EMAIL = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)


def detect_sensitive(text: str) -> list[str]:
    flags: list[str] = []
    if any(pattern.search(text) for pattern in _SECRET_PATTERNS):
        flags.append("possible_secret")
    if _EMAIL.search(text):
        flags.append("contains_email")
    return flags
