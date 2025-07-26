from app.rag.rag_pipeline import RAGPipeline
import asyncio

def test_rag_add_and_query():
    rag = RAGPipeline.get_instance()
    query = "Artificial intelligence applications"
    contexts = [
        "Artificial intelligence is transforming industries.",
        "Applications include healthcare, finance, and education.",
        "Machine learning is a key technique in AI."
    ]
    query_id = "test123"

    response = asyncio.run(rag.process(query, contexts, query_id))

    assert "artificial intelligence" in response.lower()
    assert "context" in response.lower() or "transforming" in response.lower()
    assert "\n- " in response
