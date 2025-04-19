
import pandas as pd
from experiment.experiments import run_model

def test_run_model():
    # Create a small sample dataframe with structure like your real data
    data = pd.DataFrame({
        'id': [1, 2],
        'price': [500, 1500],
        'carat': [0.3, 0.7],
        'depth': [60.0, 62.0],
        'table': [55.0, 58.0],
        'x': [4.3, 5.7],
        'y': [4.35, 5.75],
        'z': [2.7, 3.5],
        'cut': ['Ideal', 'Premium'],
        'color': ['E', 'I'],
        'clarity': ['SI1', 'VS2']
    })

    results_df = run_model(data)

    assert not results_df.empty
    assert "R²" in results_df.columns
    assert "MAE" in results_df.columns
    assert "MSE" in results_df.columns
import pandas as pd
from experiment.ml_pipeline import run_model

def test_run_model():
    # Create a small sample dataframe with structure like your real data
    data = pd.DataFrame({
        'id': [1, 2],
        'price': [500, 1500],
        'carat': [0.3, 0.7],
        'depth': [60.0, 62.0],
        'table': [55.0, 58.0],
        'x': [4.3, 5.7],
        'y': [4.35, 5.75],
        'z': [2.7, 3.5],
        'cut': ['Ideal', 'Premium'],
        'color': ['E', 'I'],
        'clarity': ['SI1', 'VS2']
    })

    results_df = run_model(data)

    assert not results_df.empty
    assert "R²" in results_df.columns
    assert "MAE" in results_df.columns
    assert "MSE" in results_df.columns
