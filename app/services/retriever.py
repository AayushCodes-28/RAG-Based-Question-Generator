from pinecone import Pinecone
from app.config import Config
from app.services.embedder import embed_text

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index = pc.Index(host=Config.PINECONE_HOST)

def retrieve_context(query: str, top_k=5):
    vector = embed_text(query)

    result = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )

    contexts = [m["metadata"]["text"] for m in result["matches"]]
    return "\n\n".join(contexts)
