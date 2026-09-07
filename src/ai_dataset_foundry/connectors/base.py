from __future__ import annotations

from abc import ABC, abstractmethod

from ai_dataset_foundry.models import DocumentRecord


class Connector(ABC):
    @abstractmethod
    def load(self, locator: str) -> list[DocumentRecord]:
        raise NotImplementedError
