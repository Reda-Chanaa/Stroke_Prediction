import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import logging


def Logistic_Regression(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series) -> LogisticRegression:
    """Trains the logistic regression model and Calculates the coefficient of determination.

    Args:
        X_train: Training data of independent features.
        X_test: Testing data of independent features.
        y_test: Testing data for stroke.
        y_train: Training data for stroke.

    Returns:
        Trained model.
        
    """

    LogisticRegressor = LogisticRegression()
    LogisticRegressor.fit(X_train, y_train)
    
    y_pred = LogisticRegressor.predict(X_test)
    score = metrics.accuracy_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient of %.3f on test data.", score)

    return LogisticRegressor