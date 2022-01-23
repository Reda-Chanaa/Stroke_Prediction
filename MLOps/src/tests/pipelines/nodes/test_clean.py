import pandas as pd
from pandas._testing import assert_frame_equal
from MLOps.pipelines.data_engineering.nodes.clean import clean

def test_encode () :
    data = pd.read_csv('data/02_intermediate/strokeData_rebase.csv')
    output = clean(data)
    found = output[output['Gender'].str.contains('Other')].Gender
    assert found.count()==0