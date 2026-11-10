from typer.testing import CliRunner

from cinecli import cli


def test_search_rejects_zero_limit_without_calling_api(monkeypatch):
    calls = []
    monkeypatch.setattr(
        cli, "search_movies", lambda query, limit: calls.append((query, limit)) or []
    )
    result = CliRunner().invoke(cli.app, ["search", "Dune", "--limit", "0"])
    assert result.exit_code == 2
    assert calls == []


def test_search_rejects_negative_limit_without_calling_api(monkeypatch):
    calls = []
    monkeypatch.setattr(
        cli, "search_movies", lambda query, limit: calls.append((query, limit)) or []
    )
    result = CliRunner().invoke(cli.app, ["search", "Dune", "--limit", "-5"])
    assert result.exit_code == 2
    assert calls == []
