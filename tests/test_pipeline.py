from hybrid_rag.pipeline import hybrid_retrieve


def test_hybrid_retrieve_returns_both_channels() -> None:
    out = hybrid_retrieve({"team": "ml"}, [{"team": "ml"}], "ml retrieval", ["ml retrieval doc", "other doc"])
    assert "structured" in out and "semantic" in out
