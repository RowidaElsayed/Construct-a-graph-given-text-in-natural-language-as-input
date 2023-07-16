Tool Name
A tool that constructs a graph given text in a natural language as input, such that a node represents a sentence, and an edge exists from one sentence (node) to another if text similarity between the two is above a user-defined threshold.
Table of Contents
•	Introduction
•	Features
•	Installation
•	Usage
•	Contributing
•	License
Introduction
The tool is designed to help users construct a graph of sentences from a text document, where each sentence is represented as a node and an edge exists between two nodes if the similarity between their corresponding sentences is above a user-defined threshold. The tool is built using Python and several libraries including NLTK, Scikit-learn, and NetworkX.
Features
•	Preprocesses the input text by removing stop words and special characters.
•	Tokenizes the input text into individual sentences.
•	Calculates the similarity between each pair of sentences using cosine similarity or Jaccard similarity.
•	Constructs a graph using sentences as nodes and the similarity between them as edges.
•	Sets a user-defined threshold for the similarity measure, and only adds edges between nodes whose similarity is above this threshold.
•	Visualizes the graph using NetworkX.



