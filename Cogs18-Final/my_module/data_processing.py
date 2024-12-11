# data_processing.py
import pandas as pd
import numpy as np

def generate_random_dataset(filename, num_rows=300):
    """
    Generates a dataset simulating human random guesses and saves it as a CSV.

    Parameters
    ----------
    filename : str
        Path to save the generated dataset.
    num_rows : int, optional
        Number of rows (default is 300).

    Returns
    -------
    pd.DataFrame
        The generated dataset.
    """
    np.random.seed(42)

    # Simulated biased guesses
    responses = np.random.choice(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        size=num_rows,
        p=[0.1, 0.15, 0.05, 0.1, 0.2, 0.1, 0.1, 0.1, 0.05, 0.05]
    )

    # Add metadata
    categories = np.random.choice(['A', 'B', 'C', 'D'], size=num_rows)
    timestamps = pd.date_range(start="2024-01-01", periods=num_rows, freq="min")

    # Combine into a DataFrame
    df = pd.DataFrame({
        'response': responses,
        'category': categories,
        'timestamp': timestamps
    })

    # Save dataset
    df.to_csv(filename, index=False)
    print("Dataset saved to: " + filename)
    return df

def load_dataset(filename):
    """
    Loads a dataset from a CSV file.

    Parameters
    ----------
    filename : str
        Path to the dataset file.

    Returns
    -------
    pd.DataFrame
        The loaded dataset.
    """
    df = pd.read_csv(filename)
    print("Loaded dataset from: " + filename)
    print("Preview:")
    print(df.head())
    return df
