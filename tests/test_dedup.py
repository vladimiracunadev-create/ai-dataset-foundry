from ai_dataset_foundry.processors.dedup import Deduplicator


def test_exact_duplicate():
    d = Deduplicator(near_duplicate=False)
    assert d.is_duplicate("hello world") is False
    assert d.is_duplicate("hello world") is True
