from pycaret import classification
from pycaret.classification import *
import pandas as pd


def pycaret_Light_GBM(df_train: pd.DataFrame,df_test: pd.DataFrame) -> classification:
    
    clf1 = setup(data = df_train,target ='stroke', test_data = df_test, silent=True, log_experiment=True, log_plots=True, experiment_name="Light GBM")
    lightgbm = create_model('lightgbm')
    lightgbm_tuned = tune_model(lightgbm, optimize='F1', n_iter= 5)

    plot_model(lightgbm_tuned, plot = 'confusion_matrix')
    plot_model(lightgbm_tuned, plot = 'auc')
    plot_model(lightgbm_tuned, plot = 'pr')

    save_model(lightgbm_tuned, './data/06_models/lightGBM')

    return lightgbm