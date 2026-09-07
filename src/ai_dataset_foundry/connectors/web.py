from __future__ import annotations

from urllib.parse import urlparse

from ai_dataset_foundry.models import DocumentRecord, SourceInfo
from ai_dataset_foundry.utils.hashing import sha256_bytes, stable_id


def load_url(url: str) -> list[DocumentRecord]:
    try:
        import requests
    except ImportError as exc:
        raise RuntimeError("Web support requires: pip install -e '.[web]'") from exc

    response = requests.get(
        url,
        timeout=30,
        headers={"User-Agent": "AI-Dataset-Foundry/0.1 (+dataset ingestion; respectful single-page fetch)"},
    )
    response.raise_for_status()
    raw = response.content
    content_type = response.headers.get("content-type", "")
    if "html" not in content_type.lower():
        text = response.text
        title = urlparse(url).path.rsplit("/", 1)[-1] or url
    else:
        try:
            import trafilatura
            text = trafilatura.extract(response.text, include_comments=False, include_tables=True) or ""
        except ImportError:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            for tag in soup(["script", "style", "noscript", "template"]):
                tag.decompose()
            text = "\n".join(s.strip() for s in soup.stripped_strings if s.strip())
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string.strip() if soup.title and soup.title.string else url
        except Exception:
            title = url
    source_hash = sha256_bytes(raw)
    return [DocumentRecord(
        id=stable_id("doc", url, source_hash),
        text=text,
        source=SourceInfo(kind="web", locator=url, title=title),
        metadata={"content_type": content_type, "status_code": response.status_code},
        source_sha256=source_hash,
    )]
