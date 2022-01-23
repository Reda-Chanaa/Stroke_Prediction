import pandas as pd
import numpy as np
import logging
from typing import Dict, Tuple
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE



logger = logging.getLogger(__name__)


def training(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """ There are categorical features in the data. So we need to encode them into numeric features

    Args:
        data (pd.DataFrame): the original inconsistent col name dataset

    Returns:
        pd.DataFrame: data set without missing values
    """
    # Split the data into X_train, X_test, y_train and y_test
    X = data.iloc[:,0:-1].values
    y = data.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    # Encoding the data
    c_t = ColumnTransformer(
        transformers=[('encoder', OneHotEncoder(), [0, 4, 7])], remainder='passthrough')
    X_train_encoded = np.array(c_t.fit_transform(X_train))
    X_test_encoded = np.array(c_t.fit_transform(X_test))
    
    # Scaling the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train_encoded)
    X_test_scaled = scaler.fit_transform(X_test_encoded)

    # Resampling the data
    sm = SMOTE(random_state=42)
    X_resampled, y_resampled = sm.fit_resample(X_train_scaled, y_train)

    # Regrouping the data
    df_train = pd.DataFrame(data=X_resampled, columns=['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'gender_Female', 'gender_Male', 'work_type_Govt_job', 'work_type_Never_worked',
                            'work_type_Private', 'work_type_Self-employed', 'work_type_children', 'smoking_status_Unknown', 'smoking_status_formerly smoked', 'smoking_status_never smoked', 'smoking_status_smokes'])
    df_ytrain = pd.DataFrame(data=y_resampled, columns=['stroke'])
    df_train['stroke'] = df_ytrain['stroke']

    df_test = pd.DataFrame(data=X_test_scaled, columns=['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi', 'gender_Female', 'gender_Male', 'work_type_Govt_job', 'work_type_Never_worked',
                           'work_type_Private', 'work_type_Self-employed', 'work_type_children', 'smoking_status_Unknown', 'smoking_status_formerly smoked', 'smoking_status_never smoked', 'smoking_status_smokes'])
    df_ytest = pd.DataFrame(data=y_test, columns=['Stroke'])
    df_test['stroke'] = df_ytest['Stroke']

    return df_train, df_test