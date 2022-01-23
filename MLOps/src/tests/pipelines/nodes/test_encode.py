import pandas as pd
from pandas._testing import assert_frame_equal
from MLOps.pipelines.data_science.nodes.Encode import encode

def test_encode () :
    data = pd.read_csv('data/02_intermediate/strokeData_clean.csv')
    output = encode(data)
    output.reset_index(drop=True)
    assert data.equals(output)