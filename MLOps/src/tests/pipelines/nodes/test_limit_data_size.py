import pandas as pd
from MLOps.pipelines.data_engineering.nodes.limit_data_size  import limit_data_size 
from pandas._testing import assert_frame_equal

def test_limit_data_size () :
    data = pd.read_csv('data/01_raw/strokeData.csv')
    output = limit_data_size(data,1200)
    output.reset_index(drop=True)
    assert len(output)==1200
    output = limit_data_size(data,None)
    output.reset_index(drop=True)
    assert len(output)==len(data)