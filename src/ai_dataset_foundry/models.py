from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class SourceInfo:
    kind: str
    locator: str
    title: str | None = None
    license: str | None = None


@dataclass(slots=True)
class Provenance:
    source_sha256: str
    content_sha256: str


@dataclass(slots=True)
class DocumentRecord:
    id: str
    text: str
    source: SourceInfo
    metadata: dict[str, Any] = field(default_factory=dict)
    source_sha256: str = ""


@dataclass(slots=True)
class QualityResult:
    score: float
    accepted: bool
    reasons: list[str] = field(default_factory=list)


@dataclass(slots=True)
class ChunkRecord:
    id: str
    document_id: str
    text: str
    source: SourceInfo
    metadata: dict[str, Any]
    provenance: Provenance
    quality: QualityResult

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
