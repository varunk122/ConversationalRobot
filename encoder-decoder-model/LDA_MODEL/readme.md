#Gensim LDA Model parameters

**corpus** —   Stream of document vectors or sparse matrix of shape (num_terms, num_documents)
**id2word** – Mapping from word IDs to words. It is used to determine the vocabulary size, as well as for debugging and topic printing.
**num_topics** — The number of requested latent topics to be extracted from the training corpus.
**random_state** — Either a randomState object or a seed to generate one. Useful for reproducibility.
**update_every** — Number of documents to be iterated through for each update. Set to 0 for batch learning, > 1 for online iterative learning.
**chunksize** — Number of documents to be used in each training chunk.
**passes** — Number of passes through the corpus during training.
**alpha** — auto: Learns an asymmetric prior from the corpus
**per_word_topics** — If True, the model also computes a list of topics, sorted in descending order of most likely topics for each word, along with their phi values multiplied by the feature-length (i.e. word count)


#About pyLDAvis

1. The size of the bubbles tells us how dominant a topic is across all the documents (our corpus)
2. The words on the right are the keywords driving that topic
3. The closer the bubbles the more similar the topic. The farther they are apart the less similar
4. Preferably, we want non-overlapping bubbles as much as possible spread across the chart.
