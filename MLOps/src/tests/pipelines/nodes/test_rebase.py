import pandas as pd
from pandas._testing import assert_frame_equal
from MLOps.pipelines.data_engineering.nodes.rebase import rebase

def test_rabase () :
    data = pd.read_csv('data/02_intermediate/strokeData_missing.csv')
    output = rebase(data)
    assert len(output.columns)==9