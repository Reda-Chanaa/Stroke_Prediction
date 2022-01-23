from kedro.pipeline import Pipeline, node

from .nodes.missing_values import missing_values
from .nodes.rename_columns import rename_columns
from .nodes.limit_data_size import limit_data_size
from .nodes.rebase import rebase
from .nodes.clean import clean

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
                inputs="strokeData_limited",
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
                func=rebase,
                inputs="strokeData_missing",
                outputs="strokeData_rebase",
                name="rebase"
                ),
            node(
                func=clean,
                inputs="strokeData_rebase",
                outputs="strokeData_cleaned",
                name="clean"
                )
        ]
        )