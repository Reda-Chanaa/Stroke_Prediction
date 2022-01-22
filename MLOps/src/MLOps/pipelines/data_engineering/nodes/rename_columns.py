from typing import Any, Dict
import pandas as pd
import logging

logger = logging.getLogger(__name__)

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