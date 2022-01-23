from typing import Any, Dict
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def clean(data: pd.DataFrame) -> pd.DataFrame:
    """ There is one row in Gender columns contains others, we should delete that row 

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: data set cleaned
    """
    df_data = data[data.Gender != 'Other']
    return df_data