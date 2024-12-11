# testing.py
from scipy.stats import chisquare

def perform_chi_square_test(data, column):
    """
    Performs a Chi-Square test to evaluate randomness.

    Parameters
    ----------
    data : pd.DataFrame
        Dataset.
    column : str
        Column to analyze.

    Returns
    -------
    tuple
        Chi-Square statistic and p-value.
    """
    observed = data[column].value_counts().values
    expected = [len(data) / len(observed)] * len(observed)
    chi2, p_value = chisquare(observed, f_exp=expected)
    return chi2, p_value
