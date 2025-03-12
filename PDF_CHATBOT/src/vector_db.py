from sentence_transformers import SentenceTransformer
import chromadb
import uuid

model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")


def get_embeddings(text):
    return model.encode(text,show_progress_bar=True).tolist()


def store_documents(chunks,session_id):
    try:

        client = chromadb.PersistentClient(path=f"data/vector_db/{session_id}")
        collection = client.get_or_create_collection(name="default")
        document_embeddings = get_embeddings(chunks)
        collection.add(
            documents=chunks,
            embeddings=document_embeddings,
            ids=[str(uuid.uuid4()) for _ in chunks]
        )
        return "success"
    
    except Exception as e:
        print(e)


def get_documents(query,session_id,n_results = 2):

    client = chromadb.PersistentClient(path=f"data/vector_db/{session_id}")
    collection = client.get_or_create_collection(name="default")
    query_embedding = get_embeddings(query)
    result  = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )
    return "\n\n".join(result["documents"][0])