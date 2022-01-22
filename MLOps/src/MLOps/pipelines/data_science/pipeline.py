from kedro.pipeline import Pipeline, node

from .nodes.split_data import split_data
from .nodes.LinearRegression import Linear_Regression
from .nodes.LogisticRegression import Logistic_Regression

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["strokeData_encoded", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="model_input",
            ),
            node(
                func=Linear_Regression,
                inputs=["X_train", "X_test", "y_train", "y_test"],
                outputs="LinearRegressor",
                name="LinearRegressor",
            ),
            node(
                func=Logistic_Regression,
                inputs=["X_train", "X_test", "y_train", "y_test"],
                outputs="LogisticRegressor",
                name="LogisticRegressor",
            ),
        ]
    )