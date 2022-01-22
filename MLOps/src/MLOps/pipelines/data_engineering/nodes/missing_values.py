from typing import Any, Dict
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """ replacing missing values in the dataset

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: data set without missing values
    """

    data['Bmi'].fillna(data['Bmi'].mean(), inplace=True)

    return data