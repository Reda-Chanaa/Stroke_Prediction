from pycaret import classification
from pycaret.classification import *
import pandas as pd


def pycaret_AdaBoost(df_train: pd.DataFrame,df_test: pd.DataFrame) -> classification:
    
    clf1 = setup(data = df_train,target ='stroke', test_data = df_test, silent=True, log_experiment=True, log_plots=True, experiment_name="AdaBoost")
    ada = create_model('ada')
    ada_tuned = tune_model(ada, optimize='F1', n_iter= 5)

    plot_model(ada_tuned, plot = 'confusion_matrix')
    plot_model(ada_tuned, plot = 'auc')
    plot_model(ada_tuned, plot = 'pr')

    save_model(ada_tuned, './data/06_models/AdaBoost')
    return ada