# convert_to_embeddings.py
"""
Script to convert conversations into embeddings and save them in a single HDF5 file.
Both embeddings and metadata are stored in the same file.
"""

import numpy as np
import h5py

# Example conversations (simulating past user interactions)
conversations = [
    "You requested an artistic image illustrating algorithmic feedback loops, specifically including references to LLMs and RL.",
    "Can you explain how reinforcement learning works in the context of LLMs?",
    "I need a summary of recent papers on Tool-augmented Reinforcement Learning (TRL).",
    "What’s the weather like today? I’m planning a trip.",
    "How can I use LLMs to improve my coding workflow?"
]

def convert_to_embeddings(conversations):
    """
    Convert a list of conversations to embeddings and create metadata.

    Args:
        conversations (list): List of conversation strings.

    Returns:
        embeddings (np.ndarray): Array of embeddings.
        metadata (list): List of metadata entries as tuples.
    """
    # Here your logic to load your model (e.g., Sentence Transformers, BERT, etc.)
    # model = ...
    
    # Simulate embedding generation (replace with actual model encoding)
    # For demonstration, we'll assume embeddings are 384-dimensional (as with all-MiniLM-L6-v2)
    embeddings = np.random.rand(len(conversations), 384)  # Placeholder: replace with model.encode(conversations)

    # Create metadata as a list of tuples (for HDF5 compound type)
    metadata = [
        (f"conv_{i}", conv, f"2025-04-{i+1} 10:00:00")
        for i, conv in enumerate(conversations)
    ]

    return embeddings, metadata

def save_data(embeddings, metadata, hdf5_file="latent_memory.h5"):
    """
    Save embeddings and metadata to a single HDF5 file.

    Args:
        embeddings (np.ndarray): Array of embeddings.
        metadata (list): List of metadata entries as tuples.
        hdf5_file (str): Path to save the HDF5 file.
    """
    # Define the compound data type for metadata
    metadata_dtype = np.dtype([
        ("conversation_id", "S10"),  # String of max length 10 (e.g., "conv_1")
        ("summary", "S200"),         # String of max length 200 for summaries
        ("timestamp", "S20")         # String of max length 20 for timestamps
    ])

    # Convert metadata to a NumPy array with the compound type
    metadata_array = np.array(metadata, dtype=metadata_dtype)

    # Save to HDF5 file
    with h5py.File(hdf5_file, 'w') as f:
        f.create_dataset('embeddings', data=embeddings)
        f.create_dataset('metadata', data=metadata_array)

    print(f"Saved embeddings and metadata to {hdf5_file}")

if __name__ == "__main__":
    # Convert conversations to embeddings
    embeddings, metadata = convert_to_embeddings(conversations)

    # Save the embeddings and metadata to HDF5
    save_data(embeddings, metadata)

    # Print for verification
    print(f"Number of embeddings: {len(embeddings)}")
    print(f"Sample embedding shape: {embeddings[0].shape}")
    print(f"Sample metadata entry: {metadata[0]}")