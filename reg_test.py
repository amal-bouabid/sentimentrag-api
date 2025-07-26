from app.rag.rag_pipeline import RAGPipeline
import asyncio

async def main():
    rag = RAGPipeline.get_instance()

    query = "What are the main applications of AI?"
    context_texts = [
        "Artificial intelligence is used in healthcare to improve diagnosis.",
        "Finance companies use AI to detect fraud and automate trading.",
        "Education platforms use AI to personalize learning."
    ]
    query_id = "test001"

    response = await rag.process(query, context_texts, query_id)
    print("\n=== RAG Response ===\n")
    print(response)

# Lancer la coroutine
asyncio.run(main())
