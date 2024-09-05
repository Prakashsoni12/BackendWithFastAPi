from sentence_transformers import SentenceTransformer,util


model = SentenceTransformer('all-MiniLM-L6-v2')


def get_relevant_response(stored_content: str, question: str) -> str:
    query_embedding = model.encode(question,convert_to_tensor=True)
    content_embedding = model.encode(stored_content,convert_to_tensor=True)

    # Calculate cosine similarity
    similarity = util.pytorch_cos_sim(query_embedding, content_embedding).item()

    # Dummy response logic based on similarity (for demonstration)
    if similarity > 0.5:  # Threshold can be adjusted based on the use case
        return "The main idea of the document is ... (based on similarity)"
    else:
        return "Sorry, I couldn't find a relevant answer."