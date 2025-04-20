# convert_to_embeddings.py
"""
Script to convert conversations into embeddings and save them as a CSV file.
Metadata is saved as a JSON file.
"""

import numpy as np
import pandas as pd
import json

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

def save_data(embeddings, metadata, embeddings_file="embeddings.csv", metadata_file="metadata.json"):
    """
    Save embeddings as a CSV file and metadata as a JSON file.

    Args:
        embeddings (np.ndarray): Array of embeddings.
        metadata (list): List of metadata entries.
        embeddings_file (str): Path to save embeddings.
        metadata_file (str): Path to save metadata.
    """
    # Convert embeddings to a DataFrame and save as CSV
    embeddings_df = pd.DataFrame(embeddings)
    embeddings_df.to_csv(embeddings_file, index=False)

    # Save metadata as JSON
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    print(f"Saved embeddings to {embeddings_file} and metadata to {metadata_file}")

if __name__ == "__main__":
    # Convert conversations to embeddings
    embeddings, metadata = convert_to_embeddings(conversations)

    # Save the embeddings and metadata
    save_data(embeddings, metadata)

    # Print for verification
    print(f"Number of embeddings: {len(embeddings)}")
    print(f"Sample embedding shape: {embeddings[0].shape}")
    print(f"Sample metadata entry: {metadata[0]}")