# visualization.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_response_distribution(data):
    """
    Plots a histogram of responses.

    Parameters
    ----------
    data : pd.DataFrame
        Dataset with the 'response' column.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data['response'], bins=10, kde=False, color='blue')
    plt.title("Response Distribution")
    plt.xlabel("Response")
    plt.ylabel("Frequency")
    plt.show()
