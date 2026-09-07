from ai_dataset_foundry.connectors import git as git_connector
from ai_dataset_foundry.connectors.router import ingest


def test_github_repository_url_uses_git_connector(monkeypatch):
    seen = []

    def fake_load_git(locator):
        seen.append(locator)
        return []

    monkeypatch.setattr(git_connector, "load_git", fake_load_git)
    locator = "https://github.com/example/training-corpus"
    assert ingest(locator) == []
    assert seen == [locator]
