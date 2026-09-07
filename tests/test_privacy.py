from ai_dataset_foundry.processors.privacy import detect_sensitive


def test_email_flag():
    assert "contains_email" in detect_sensitive("write to test@example.com")


def test_secret_flag():
    assert "possible_secret" in detect_sensitive("api_key = abcdefghijklmnop123456")
