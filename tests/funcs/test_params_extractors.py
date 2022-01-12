from src.funcs.params_extractors import sample_number_extractor, voltage_extractor, duration_min_extractor, user_extractor, get_mod_date_of_file

class TestSampleNumberExtractor(object):

    def test_with_clean_salt_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 1 HRS SALTBJC.txt"
        
        expected = 20
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_tapwater_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 13 MIN TAPBJC.txt"
        
        expected = 20
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\empty_file.txt"
        
        expected = None
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\random_text.txt"
        
        expected = None
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

