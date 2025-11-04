def search_structured(filters: dict[str, str], rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out = []
    for row in rows:
        if all(row.get(k) == v for k, v in filters.items()):
            out.append(row)
    return out
