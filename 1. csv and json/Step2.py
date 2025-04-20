# store_in_vector_db.py
"""
Script to store embeddings in a FAISS vector database for efficient semantic search.
Loads embeddings from a CSV file and metadata from a JSON file.
"""

import numpy as np
import pandas as pd
import faiss
import json

def load_data(embeddings_file="embeddings.csv", metadata_file="metadata.json"):
    """
    Load embeddings and metadata from files.

    Args:
        embeddings_file (str): Path to embeddings CSV file.
        metadata_file (str): Path to metadata JSON file.

    Returns:
        embeddings (np.ndarray): Array of embeddings.
        metadata (list): List of metadata entries.
    """
    # Load embeddings from CSV
    embeddings = pd.read_csv(embeddings_file).to_numpy()

    # Load metadata from JSON
    with open(metadata_file, 'r') as f:
        metadata = json.load(f)

    return embeddings, metadata

def create_faiss_index(embeddings, index_file="faiss_index.bin"):
    """
    Create a FAISS index from embeddings and save it.

    Args:
        embeddings (np.ndarray): Array of embeddings.
        index_file (str): Path to save the FAISS index.

    Returns:
        index (faiss.Index): FAISS index for semantic search.
    """
    # Ensure embeddings are in the correct format (float32)
    embeddings = embeddings.astype('float32')

    # Get the dimension of the embeddings
    dimension = embeddings.shape[1]

    # Create a FAISS index (using Inner Product for cosine similarity)
    index = faiss.IndexFlatIP(dimension)

    # Add embeddings to the index
    index.add(embeddings)

    # Save the index
    faiss.write_index(index, index_file)
    print(f"Saved FAISS index to {index_file}")

    return index

if __name__ == "__main__":
    # Load embeddings and metadata
    embeddings, metadata = load_data()

    # Create and save the FAISS index
    index = create_faiss_index(embeddings)

    # Verify the index
    print(f"Number of vectors in FAISS index: {index.ntotal}")