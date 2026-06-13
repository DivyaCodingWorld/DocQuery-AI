import faiss, numpy as np
index = None
stored_chunks = []

def store_embeddings(chunks, embeddings):
    global index, stored_chunks
    embeddings = np.array(embeddings).astype("float32")
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    stored_chunks = chunks

def search_similar_chunks(query_embedding, top_k=3):
    global index, stored_chunks
    if index is None:
        return []
    q = np.array([query_embedding]).astype("float32")
    _, indices = index.search(q, top_k)
    return [stored_chunks[i] for i in indices[0] if i < len(stored_chunks)]
