# tests/test_analysis.py
import pytest
from my_module.analysis import calculate_metrics

def test_calculate_metrics():
    import pandas as pd
    data = pd.DataFrame({'response': [1, 2, 2, 3, 3, 3]})
    metrics = calculate_metrics(data, 'response')

    assert metrics['num_unique'] == 3
    assert metrics['num_total'] == 6
    assert metrics['most_common'] == 3
    assert metrics['count_most_common'] == 3
