# clean_chroma.py
from chromadb import PersistentClient
from app.common.config import Config

client = PersistentClient(path=str(Config.CHROMA_PATH))
collection = client.get_or_create_collection(name="rag_collection")

# Supprime toute la collection
collection.delete()
print("✅ Collection ChromaDB vidée.")
