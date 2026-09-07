from __future__ import annotations

from ai_dataset_foundry.config import QualityConfig
from ai_dataset_foundry.models import QualityResult
from ai_dataset_foundry.processors.privacy import detect_sensitive


def assess_quality(text: str, config: QualityConfig) -> QualityResult:
    reasons: list[str] = []
    if len(text) < config.min_chars:
        reasons.append("too_short")

    controls = sum(1 for c in text if ord(c) < 32 and c not in "\n\t")
    ratio = controls / max(1, len(text))
    if ratio > config.max_control_ratio:
        reasons.append("too_many_control_characters")

    sensitive = detect_sensitive(text)
    if config.reject_secrets and "possible_secret" in sensitive:
        reasons.append("possible_secret")

    score = 1.0
    if "too_short" in reasons:
        score -= 0.45
    if "too_many_control_characters" in reasons:
        score -= 0.35
    if "possible_secret" in reasons:
        score -= 0.8
    return QualityResult(score=max(0.0, round(score, 3)), accepted=not reasons, reasons=reasons + [f"flag:{x}" for x in sensitive if x not in reasons])
