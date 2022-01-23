from typing import Any, Dict
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def rebase(data: pd.DataFrame) -> pd.DataFrame:
    """ delete features no needed

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: data set without id, ever_married and Residence_type columns
    """
    data.drop(columns=['Id','Ever_married','Residence_type'], inplace = True)

    return data