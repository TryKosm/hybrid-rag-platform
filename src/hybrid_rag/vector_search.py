def rank_documents(query: str, docs: list[str]) -> list[str]:
    q = set(query.lower().split())
    return sorted(
        docs,
        key=lambda d: (len(q.intersection(set(d.lower().split()))), -len(d)),
        reverse=True,
    )
