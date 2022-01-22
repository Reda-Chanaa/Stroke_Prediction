from kedro.pipeline import Pipeline, node

from .nodes import limit_data_size
from .nodes import rename_column

def create_pipeline(**kwargs):
    # Create the pipeline that will transfer the appropriate
    # data to the proper locations.
    return Pipeline(
        [
            node(
                func=limit_data_size,
                inputs=["strokeData", "params:limit_size"],
                outputs="strokeData_limited",
                name="limit_data_size"
                ),
            node(
                func=rename_column,
                inputs="strokeData",
                outputs="strokeData_renamed",
                name="rename_column"
                ),
        ]
        )