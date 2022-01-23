from kedro.pipeline import Pipeline, node

from .nodes.split_data import split_data
from .nodes.LogisticRegression import Logistic_Regression
from .nodes.pycaret import pycaret_classification
from .nodes.AdaBoost import AB_Classifier
from .nodes.SVC import SVC_Classifier

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
                func=Logistic_Regression,
                inputs=["X_train", "X_test", "y_train", "y_test"],
                outputs="LogisticRegressor",
                name="LogisticRegressor",
            ),
            node(
                func=AB_Classifier,
                inputs=["X_train", "X_test", "y_train", "y_test"],
                outputs="AdaClassifier",
                name="AdaClassifier",
            ),
            
        ]
    )

"""
            node(
                func=pycaret_classification,
                inputs=["strokeData_encoded"],
                outputs="pycaret_classification",
                name="pycaret_classification",
            ),
            node(
                func=SVC_Classifier,
                inputs=["X_train", "X_test", "y_train", "y_test"],
                outputs="SVC_CLaassifier",
                name="SVC_CLaassifier",
            ),"""