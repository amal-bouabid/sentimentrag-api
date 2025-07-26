# app/rag/vector_db.py
from chromadb import PersistentClient
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from app.common.config import Config
import logging

logger = logging.getLogger(__name__)

class ChromaVectorDB:
    def __init__(self):
        settings = Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=str(Config.CHROMA_PATH),
            anonymized_telemetry=False
        )
        try:
            self.client = PersistentClient(settings=settings)
            self.collection = self.client.get_or_create_collection("contexts")
            self.encoder = SentenceTransformer(Config.EMBEDDING_MODEL)
            logger.info("VectorDB initialized successfully")
        except Exception as e:
            logger.error(f"VectorDB init failed: {e}")
            raise

    def add_contexts(self, texts, ids):
        try:
            embeddings = self.encoder.encode(texts).tolist()
            self.collection.add(documents=texts, embeddings=embeddings, ids=ids)
            logger.info(f"Added {len(texts)} contexts to DB")
        except Exception as e:
            logger.error(f"Failed to add contexts: {e}")

    def query(self, text, n_results=2):
        try:
            embedding = self.encoder.encode(text).tolist()
            results = self.collection.query(query_embeddings=[embedding], n_results=n_results)
            return results["documents"][0] if results["documents"] else []
        except Exception as e:
            logger.error(f"Query failed: {e}")
            return []
