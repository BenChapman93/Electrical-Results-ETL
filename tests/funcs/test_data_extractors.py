from src.funcs.data_extractors import txt_to_df
import pandas as pd

class TestTxtToDf(object):

    def test_with_clean_tapwater_file(self):

        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 13 MIN TAPBJC.txt"

        expected = True
        actual = isinstance(txt_to_df(file), pd.core.frame.DataFrame)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message