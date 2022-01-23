
import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
import logging
from sklearn import metrics


def AB_Classifier(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.Series, y_test: pd.Series) -> AdaBoostClassifier:

    abc = AdaBoostClassifier(n_estimators=50,
                             learning_rate=1)
    # Train Adaboost Classifer
    model = abc.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = model.predict(X_test)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient of %.3f on test data.", metrics.accuracy_score(y_test, y_pred))
    return model