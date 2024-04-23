from sklearn.metrics.pairwise import cosine_similarity
import pickle
# Load the saved objects
with open('tfidf_matrix.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('urls.pkl', 'rb') as file:
    urls = pickle.load(file)

def handle_query(query, top_k=5):
    # Convert the query to a TF-IDF vector
    query_vector = vectorizer.transform([query])

    # Calculate cosine similarity between the query vector and the TF-IDF matrix
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

    # Get the indices of the top-K most similar documents
    top_k_indices = similarity_scores.argsort()[-top_k:][::-1]

    print(top_k_indices)

    # Retrieve the URLs of the top-K most similar documents
    top_k_urls = [urls[i] for i in top_k_indices]

    return top_k_urls

# Example usage
query = 'Son Heung-min'
top_k_urls = handle_query(query, top_k=5)

print("\n\n\n")
print("Query:", query)
print('Top 5 most relevant URLs:', top_k_urls)
