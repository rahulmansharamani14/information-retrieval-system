from flask import Flask, render_template, redirect, jsonify, request
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
from query_procesor import *


app = Flask(__name__)
# Enable CORS for the Flask app
CORS(app)

# Load saved objects: TF-IDF matrix, vectorizer, and URLs
with open('../indexer/tfidf_matrix.pkl', 'rb') as file:
    tfidf_matrix = pickle.load(file)

with open('../indexer/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('../indexer/urls.pkl', 'rb') as file:
    urls = pickle.load(file)

@app.route('/', methods=['GET'])
def index():
    return jsonify({'top_k_urls': 2})
  
# @app.route("/search", methods = ['POST'])
# def search():
    
#     print('search')
#     data = request.get_json()
    
#     # Extract the query from the JSON payload
#     query = data['query']
#     top_k = data['top_k']

#     # Transform the query into a TF-IDF vector using the vectorizer
#     query_vector = vectorizer.transform([query])
    
#     # Calculate cosine similarity between the query vector and the TF-IDF matrix
#     similarity_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

#     # Get the indices of the top-K most similar documents
#     top_k_indices = similarity_scores.argsort()[-top_k:][::-1]

#     # Retrieve the URLs of the top-K most similar documents
#     top_k_urls = [urls[i] for i in top_k_indices]

#     # Return the top-K URLs as a JSON response
#     return jsonify({'top_k_urls': top_k_urls})
    


@app.route("/search", methods = ['POST'])
def result():
    index = load_index('../Indexer/inverted_index.pickle')
    corpus, urls = load_corpus_file('../indexer/corpus.txt'), load_urls('../Indexer/urls.txt')
    
    # K = 10

    search = request.get_json()['query']
    K = request.get_json()['top_k']

    # search = spelling_correction(search)[:-1]
    query = modify_query(search, get_vocab(index))[:-1]

    print("query", query)

    vector = query_to_vector(query, index, len(corpus))

    print("vector", vector)

    matches = cos_similarity(vector, index, corpus)

    print(query)
    print(matches[:K])
    top_k = matches[:K]

    results = []

    for i in range(len(top_k)):
        # results += urls[matches[i][0]] + '\n'
        doc = {
            'url': urls[top_k[i][0]],
            'score': top_k[i][1],
            'docId': top_k[i][0],
        }
        results.append(doc)
    return jsonify(results)





if __name__ == '__main__':
    app.run(debug=True, port=3000)