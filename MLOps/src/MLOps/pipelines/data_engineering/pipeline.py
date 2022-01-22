from kedro.pipeline import Pipeline, node

from .nodes import limit_data_size, missing_values,rename_columns, encode

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
                func=rename_columns,
                inputs="strokeData",
                outputs="strokeData_renamed",
                name="rename_columns"
                ),
            node(
                func=missing_values,
                inputs="strokeData_renamed",
                outputs="strokeData_missing",
                name="missing_values"
                ),
            node(
                func=encode,
                inputs="strokeData_missing",
                outputs="strokeData_encoded",
                name="encode"
                ),
        ]
        )