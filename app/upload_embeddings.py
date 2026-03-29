from pinecone import Pinecone
from app.services.embedder import embed_text
from app.config import Config
import json

pc = Pinecone(api_key=Config.PINECONE_API_KEY)
index = pc.Index(host=Config.PINECONE_HOST)

data = json.load(open("data/domain_notes.json"))

vectors = []

for item in data:
    vectors.append({
        "id": item["id"],
        "values": embed_text(item["text"]),
        "metadata": {
            "text": item["text"]
        }
    })

index.upsert(vectors)
print("Uploaded embeddings to Pinecone!")
