from ai_dataset_foundry.processors.chunk import chunk_text


def test_fixed_chunks_overlap():
    text = "abcdefghijklmnopqrstuvwxyz"
    chunks = chunk_text(text, "fixed", 10, 2)
    assert chunks[0] == "abcdefghij"
    assert chunks[1].startswith("ij")


def test_paragraph_packing():
    text = "A" * 50 + "\n\n" + "B" * 50
    chunks = chunk_text(text, "paragraph", 60)
    assert len(chunks) == 2
