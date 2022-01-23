from kedro.pipeline import Pipeline, node

from .nodes.Mlflow_Random_Forest import pycaret_random_forest
from .nodes.Mlflow_AdaBoost import pycaret_AdaBoost
from .nodes.Mlflow_Light_GBM import pycaret_Light_GBM
from .nodes.Training import training

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=training,
                inputs=["strokeData_cleaned", "parameters"],
                outputs=["df_train", "df_test"],
                name="training"
            ),
            node(
                func=pycaret_AdaBoost,
                inputs=["df_train","df_test"],
                outputs="pycaret_AdaBoost",
                name="pycaret_AdaBoost",
            ),
            node(
                func=pycaret_random_forest,
                inputs=["df_train","df_test"],
                outputs="pycaret_random_forest",
                name="pycaret_random_forest",
            ),
            node(
                func=pycaret_Light_GBM,
                inputs=["df_train","df_test"],
                outputs="pycaret_Light_GBM",
                name="pycaret_Light_GBM",
            ),
            
        ]
    )