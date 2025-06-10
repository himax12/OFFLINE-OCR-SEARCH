from whoosh import index
from whoosh.qparser import QueryParser

INDEX_DIR = "indexdir"

def search_index(query_str):
    ix = index.open_dir(INDEX_DIR)
    qp = QueryParser("content", schema=ix.schema)
    results_list = []

    with ix.searcher() as searcher:
        query = qp.parse(query_str)
        results = searcher.search(query, limit=10)

        for r in results:
            results_list.append((r['title'], r.highlights("content")))

    return results_list
