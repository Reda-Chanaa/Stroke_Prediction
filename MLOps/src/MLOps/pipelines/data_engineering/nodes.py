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

    """
    1) id: unique identifier
    2) gender: "Male", "Female" or "Other"
    3) age: age of the patient
    4) hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
    5) heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
    6) ever_married: "No" or "Yes"
    7) work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
    8) Residence_type: "Rural" or "Urban"
    9) avg_glucose_level: average glucose level in blood
    10) bmi: body mass index
    11) smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
    12) stroke: 1 if the patient had a stroke or 0 if not

    *Note: "Unknown" in smoking_status means that the information is unavailable for this patient
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

def missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """ removing the missing values form dataset

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: data set without missing values
    """

    return data.dropna(subset=['bmi'])

def summarize(data: pd.DataFrame) -> pd.DataFrame:
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

    data['RestingECG'].replace('ST', 1,inplace=True)
    data['RestingECG'].replace('LVH', 2,inplace=True)
    data['ExerciseAngina'].replace('Y', 1,inplace=True)
    data['ExerciseAngina'].replace('N', 0,inplace=True)
    data['ST_Slope'].replace('Up', 1,inplace=True)
    data['ST_Slope'].replace('Flat', 0,inplace=True)
    data['ST_Slope'].replace('Down', 2,inplace=True)

    return data
