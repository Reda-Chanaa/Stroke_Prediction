import pandas as pd
from MLOps.pipelines.data_engineering.nodes.rename_columns  import rename_columns 
from pandas._testing import assert_frame_equal

def test_rename_columns () :
    data = pd.read_csv('data/02_intermediate/strokeData_missing.csv')
    output = rename_columns(data)
    output.reset_index(drop=True)
    assert "Id" in output.columns
    assert "Gender" in output.columns
    assert "Age" in output.columns
    assert "Hypertension" in output.columns
    assert "Heart_disease" in output.columns
    assert "Ever_married" in output.columns
    assert "Work_type" in output.columns
    assert "Residence_type" in output.columns
    assert "Avg_glucose_level" in output.columns
    assert "Bmi" in output.columns
    assert "Smoking_status" in output.columns
    assert "Stroke" in output.columns