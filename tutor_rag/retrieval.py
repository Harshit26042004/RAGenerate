import re
import nltk
import gensim
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def clear_list(documents):
  for sent in documents:
    if len(sent)==0:
      documents.remove(sent)
  return documents

def preprocess(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())  # Tokenization
    words = [word for word in words if word not in stop_words and word.isalpha()]  # Remove stopwords
    return words

class Retrieval:
    def __init__(self, documents):
        documents = re.split("[.\n]",documents)
        self.documents = clear_list(documents)
        self.processed_docs = [preprocess(doc) for doc in documents]
        self.processed_docs = clear_list(self.processed_docs)

        self.model = Word2Vec(self.processed_docs, vector_size=100, window=5, min_count=1, workers=4)

    def ask_query(self, query, n_query):
        query_tokens = preprocess(query)
        query_tokens = clear_list(query_tokens)

        for word in query_tokens:
            try:
                k = self.model.wv[word]
            except:
                print("Oops!!\nNo such word found!")
                continue
            if word not in self.model.wv:
                continue
            
            query_vector = sum([self.model.wv[word]]) / len(query_tokens)

        similarities = []
        for doc in self.documents:
            doc_tokens = preprocess(doc)
            if len(doc_tokens)==0:
                continue
            doc_tokens = clear_list(doc_tokens)
            doc_vector = sum([self.model.wv[word] for word in doc_tokens if word in self.model.wv]) / len(doc_tokens)
            similarity = cosine_similarity([query_vector], [doc_vector])[0][0]
            similarities.append((doc, similarity))

        if n_query > len(similarities):
            n_query = len(similarities)-1

        return sorted(similarities, key=lambda x: x[1], reverse=True)[:n_query]
