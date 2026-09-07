from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

from ai_dataset_foundry.utils.hashing import sha256_text


def _tokens(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())


def simhash(text: str, bits: int = 64) -> int:
    vector = [0] * bits
    for token in _tokens(text):
        h = int.from_bytes(hashlib.blake2b(token.encode(), digest_size=8).digest(), "big")
        for i in range(bits):
            vector[i] += 1 if (h >> i) & 1 else -1
    value = 0
    for i, weight in enumerate(vector):
        if weight >= 0:
            value |= 1 << i
    return value


def hamming(a: int, b: int) -> int:
    return (a ^ b).bit_count()


@dataclass
class Deduplicator:
    near_duplicate: bool = True
    max_distance: int = 3
    exact_seen: set[str] = field(default_factory=set)
    hashes: list[int] = field(default_factory=list)

    def is_duplicate(self, text: str) -> bool:
        exact = sha256_text(text)
        if exact in self.exact_seen:
            return True
        candidate = simhash(text)
        if self.near_duplicate and any(hamming(candidate, known) <= self.max_distance for known in self.hashes):
            return True
        self.exact_seen.add(exact)
        self.hashes.append(candidate)
        return False
