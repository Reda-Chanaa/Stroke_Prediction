from typing import Any, Dict
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def encode(data: pd.DataFrame) -> pd.DataFrame:
    """ There are categorical features in the data. So we need to encode them into numeric features

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: data set without missing values
    """
    #for Gender column
    data['Gender'].replace("Female", 0,inplace=True)
    data['Gender'].replace('Male', 1,inplace=True)
    data['Gender'].replace('Other', 2,inplace=True)

    # for Ever_married column
    data['Ever_married'].replace('No', 0,inplace=True)
    data['Ever_married'].replace("Yes", 1,inplace=True)

    # for Work_type column 
    data['Work_type'].replace("Private", 0,inplace=True)
    data['Work_type'].replace('children', 1,inplace=True)
    data['Work_type'].replace('Self-employed', 2,inplace=True)
    data['Work_type'].replace('Govt_job', 3,inplace=True)
    data['Work_type'].replace('Never_worked', 4,inplace=True)
    
    # for Residence_type column
    data['Residence_type'].replace('Rural', 0,inplace=True)
    data['Residence_type'].replace("Urban", 1,inplace=True)

    # for Smoking_status column
    data['Smoking_status'].replace("never smoked", 0,inplace=True)
    data['Smoking_status'].replace('smokes', 1,inplace=True)
    data['Smoking_status'].replace('formerly smoked', 2,inplace=True)
    data['Smoking_status'].replace('Unknown', 3,inplace=True)

    return data
