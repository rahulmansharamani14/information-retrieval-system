import numpy as np
import nltk
from collections import defaultdict
from itertools import groupby
import pickle
import math
nltk.download('words')
from nltk.corpus import words
correct_words = words.words()


def load_index(pickle_file):
    with open(pickle_file, 'rb') as f:
        dict = pickle.load(f)
    return dict

def load_corpus_file(corpus_file):
    with open(corpus_file, 'r') as f:
        lines = f.readlines()
    return lines
    
def load_urls(url_file):
    with open(url_file, 'r') as f:
        lines = f.readlines()
    return lines

def get_vocab(index):
    return [term for term in index.keys()]

def spelling_correction(query):
    corrected_query = ''
    for word in query.split():
        temp = [(nltk.edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]
        corrected_query += sorted(temp, key = lambda val:val[0])[0][1] + ' '
    return corrected_query


def modify_query(query, vocab):
    query_terms = query.split() 
    modified_query = ''
    for term in query_terms:
        match = vocab[0]
        min_dst = nltk.edit_distance(term, match)
        for i in range(1, len(vocab)):
            dst = nltk.edit_distance(term, vocab[i])
            if  dst < min_dst:
                min_dst = dst
                match = vocab[i]
        modified_query += match + ' '
    
    return modified_query


def query_to_vector(query, inv_index, N):
    terms = query.split(" ")
    vector = {}
    for term in terms:
        if term not in inv_index:
            vector[term] = 0
        else:
            df = len(inv_index[term])
            idf = math.log(N / df)
            vector[term] = idf
    return vector

def cos_similarity(query_vector, tfidf_index, corpus):
    scores = {}
    for i in range(len(corpus)):
        scores[i] = 0
    for term in query_vector:
        for (doc, score) in tfidf_index[term]:
            scores[doc] += score * query_vector[term]
    for doc in scores.keys():
        scores[doc] = scores[doc] / len(corpus[doc])

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

# a= spelling_correction("quezy")
# print(a)