from .schema_search import search_structured
from .vector_search import rank_documents


def hybrid_retrieve(filters: dict[str, str], rows: list[dict[str, str]], query: str, docs: list[str]) -> dict[str, object]:
    return {
        "structured": search_structured(filters, rows),
        "semantic": rank_documents(query, docs)[:3],
    }
