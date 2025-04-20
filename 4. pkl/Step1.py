# convert_to_embeddings.py
"""
Script to convert conversations into embeddings and save them in a single .pkl file.
Both embeddings and metadata are stored in the same file using pickle.
"""

import numpy as np
import pickle

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
        metadata (list): List of metadata entries as dicts.
    """
    # Here your logic to load your model (e.g., Sentence Transformers, BERT, etc.)
    # model = ...
    
    # Simulate embedding generation (replace with actual model encoding)
    # For demonstration, we'll assume embeddings are 384-dimensional (as with all-MiniLM-L6-v2)
    embeddings = np.random.rand(len(conversations), 384)  # Placeholder: replace with model.encode(conversations)

    # Create metadata for each conversation
    metadata = [
        {
            "conversation_id": f"conv_{i}",
            "summary": conv,
            "timestamp": f"2025-04-{i+1} 10:00:00"
        }
        for i, conv in enumerate(conversations)
    ]

    return embeddings, metadata

def save_data(embeddings, metadata, pickle_file="latent_memory.pkl"):
    """
    Save embeddings and metadata to a single .pkl file.

    Args:
        embeddings (np.ndarray): Array of embeddings.
        metadata (list): List of metadata entries.
        pickle_file (str): Path to save the .pkl file.
    """
    # Create a dictionary to store both embeddings and metadata
    data = {
        "embeddings": embeddings,
        "metadata": metadata
    }

    # Save to .pkl file using pickle
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f)

    print(f"Saved embeddings and metadata to {pickle_file}")

if __name__ == "__main__":
    # Convert conversations to embeddings
    embeddings, metadata = convert_to_embeddings(conversations)

    # Save the embeddings and metadata to .pkl
    save_data(embeddings, metadata)

    # Print for verification
    print(f"Number of embeddings: {len(embeddings)}")
    print(f"Sample embedding shape: {embeddings[0].shape}")
    print(f"Sample metadata entry: {metadata[0]}")