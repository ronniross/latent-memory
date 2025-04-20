# store_in_vector_db.py
"""
Script to store embeddings in a FAISS vector database for efficient semantic search.
Loads embeddings and metadata from a single HDF5 file.
"""

import numpy as np
import faiss
import h5py

def load_data(hdf5_file="latent_memory.h5"):
    """
    Load embeddings and metadata from a single HDF5 file.

    Args:
        hdf5_file (str): Path to the HDF5 file.

    Returns:
        embeddings (np.ndarray): Array of embeddings.
        metadata (np.ndarray): Structured array of metadata.
    """
    with h5py.File(hdf5_file, 'r') as f:
        embeddings = np.array(f['embeddings'])
        metadata = np.array(f['metadata'])

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
    # Load embeddings and metadata from HDF5
    embeddings, metadata = load_data()

    # Create and save the FAISS index
    index = create_faiss_index(embeddings)

    # Verify the index
    print(f"Number of vectors in FAISS index: {index.ntotal}")