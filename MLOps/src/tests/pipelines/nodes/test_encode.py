import pandas as pd
from MLOps.pipelines.data_engineering.nodes.encode  import encode 
from pandas._testing import assert_frame_equal

def test_encode () :
    data = pd.read_csv('data/02_intermediate/strokeData_missing.csv')
    output = encode(data)
    output.reset_index(drop=True)
    assert data.equals(output)