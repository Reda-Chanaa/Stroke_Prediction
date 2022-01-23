import pandas as pd
from MLOps.pipelines.data_engineering.nodes.missing_values  import missing_values 

def test_missing_values () :
    data = pd.read_csv('data/02_intermediate/strokeData_renamed.csv')
    output = missing_values(data)
    assert output.isnull().values.any() == False