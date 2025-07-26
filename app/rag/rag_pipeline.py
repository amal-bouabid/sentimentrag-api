from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from app.common.config import Config

class RAGPipeline:
    _instance = None

    def __init__(self):
        # Initialise SentenceTransformer pour l'embedding
        self.model = SentenceTransformer(Config.EMBEDDING_MODEL)

        # Initialise le client Chroma avec la nouvelle API (v1.0.15+)
        self.client = PersistentClient(path=str(Config.CHROMA_PATH))

        # Crée ou récupère une collection (Chroma s’occupe de la persistance)
        self.collection = self.client.get_or_create_collection(name="rag_collection")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    async def process(self, query: str, context_texts: list[str], query_id: str) -> str:
        # Ajoute les documents dans la base
        self.collection.add(
            documents=context_texts,
            ids=[f"{query_id}_{i}" for i in range(len(context_texts))],
            metadatas=[{"source": "user"} for _ in context_texts]
        )

        # Fait une requête sur les documents
        results = self.collection.query(
            query_texts=[query],
            n_results=3
        )

        # Récupère les documents les plus pertinents
        relevant_docs = results.get("documents", [[]])[0]

        response = "Here is a response based on the most relevant context:\n"
        for doc in relevant_docs:
            response += f"- {doc}\n"

        return response