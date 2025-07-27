# app/rag/rag_pipeline.py

from app.rag.vector_db import ChromaVectorDB
import uuid

class RAGPipeline:
    _instance = None

    def __init__(self):
        # Initialise une seule fois la base vectorielle via vector_db.py
        self.db = ChromaVectorDB()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    async def process(self, query: str, context_texts: list[str], query_id: str = None) -> str:
        try:
            # Génère un ID unique si non fourni
            if not query_id:
                query_id = str(uuid.uuid4())

            # Ajoute les contextes dans la base (avec IDs uniques)
            self.db.add_contexts(
                texts=context_texts,
                ids=[f"{query_id}_{i}" for i in range(len(context_texts))]
            )

            # Recherche les documents les plus pertinents (par embedding)
            results = self.db.query(text=query, n_results=1)

            # Supprime les doublons dans les résultats, tout en conservant l'ordre
            seen = set()
            unique_results = []
            for doc in results:
                if doc not in seen:
                    unique_results.append(doc)
                    seen.add(doc)

            # Construction de la réponse textuelle
            if unique_results:
                response = "Here is a response based on the most relevant context: "
                for doc in unique_results:
                    response += f"- {doc}"
            else:
                response = "No relevant context found."

            return response

        except Exception as e:
            return f"Error in RAG process: {str(e)}"
