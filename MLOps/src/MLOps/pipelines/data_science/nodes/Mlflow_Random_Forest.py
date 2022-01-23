from pycaret import classification
from pycaret.classification import *
import pandas as pd


def pycaret_random_forest(df_train: pd.DataFrame,df_test: pd.DataFrame) -> classification:
    
    clf1 = setup(data = df_train,target ='stroke', test_data = df_test, silent=True, log_experiment=True, log_plots=True, experiment_name="Random Forest")
    rf = create_model('rf')
    rf_tuned = tune_model(rf, optimize='F1', n_iter= 5)
    plot_model(rf_tuned, plot = 'confusion_matrix')
    plot_model(rf_tuned, plot = 'auc')
    plot_model(rf_tuned, plot = 'pr')

    save_model(rf_tuned, './data/06_models/Random_Forest')
    return rf