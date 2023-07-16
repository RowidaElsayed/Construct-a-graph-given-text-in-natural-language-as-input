import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

# Input text
input_text = "This is the first sentence. This is the second sentence. This is the third sentence."

# Preprocessing
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
  tokens = word_tokenize(text.lower())
  filtered_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words and token.isalpha()]
  return ' '.join(filtered_tokens)

sentences = sent_tokenize(input_text)
preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]

# Text Similarity Calculation
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(preprocessed_sentences)
similarity_matrix = cosine_similarity(vectors, dense_output=False)

# Graph Construction
threshold = 0.2
graph = nx.Graph()

for i, node_i in enumerate(sentences):
  for j, node_j in enumerate(sentences):
    if i < j and similarity_matrix[i, j] > threshold:
      graph.add_edge(node_i, node_j, weight=similarity_matrix[i, j])

# Visualizing the Graph
pos = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph, pos, node_size=100)
nx.draw_networkx_edges(graph, pos, alpha=0.5)
nx.draw_networkx_labels(graph, pos, font_size=10, font_family='sans-serif')
plt.axis('off')
plt.show()