from typing import Any, Dict
import pandas as pd
import logging

logger = logging.getLogger(__name__)


def limit_data_size(data: pd.DataFrame, limit_size: int) -> pd.DataFrame:
    """ Limit the number of row the initial dataset OR
        return the same dataset if *limit_size* param is null

    Args:
        data (pd.DataFrame): the initial loaded dataset
        limit_size (int): number of rows

    Returns:
        pd.DataFrame: the limited dataset n first rows or the initial dataset if limit_size is null
    """

    if limit_size is None:
        logger.warning("No limit size provided, full data will be used")
        return data

    return data.head(limit_size)


def rename_columns(data: pd.DataFrame) -> pd.DataFrame:
    """ Rename the original column names into camelCase

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: camelCase col name dataset
    """
    new_names = [
        "Id",
        "Gender",
        "Age",
        "Hypertension",
        "Heart_disease",
        "Ever_married",
        "Work_type",
        "Residence_type",
        "Avg_glucose_level",
        "Bmi",
        "Smoking_status",
        "Stroke"
    ]
    data.columns = new_names

    return data
