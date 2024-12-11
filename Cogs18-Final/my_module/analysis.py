# analysis.py
from sklearn.cluster import KMeans

def calculate_metrics(data, column):
    """
    Calculates randomness metrics for a given column.

    Parameters
    ----------
    data : pd.DataFrame
        The dataset.
    column : str
        Column to analyze.

    Returns
    -------
    dict
        Randomness metrics.
    """
    num_unique = data[column].nunique()
    num_total = len(data[column])
    proportion_unique = num_unique / num_total
    most_common = data[column].mode()[0]
    count_most_common = data[column].value_counts().iloc[0]

    return {
        'num_unique': num_unique,
        'num_total': num_total,
        'proportion_unique': proportion_unique,
        'most_common': most_common,
        'count_most_common': count_most_common
    }

def perform_clustering(data, column, n_clusters=3):
    """
    Performs K-Means clustering on a column.

    Parameters
    ----------
    data : pd.DataFrame
        Dataset.
    column : str
        Column to cluster.
    n_clusters : int, optional
        Number of clusters (default is 3).

    Returns
    -------
    pd.DataFrame
        Dataset with cluster labels.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    data['cluster'] = kmeans.fit_predict(data[[column]])
    print("Clustering complete. Added 'cluster' column with " + str(n_clusters) + " clusters.")
    return data
