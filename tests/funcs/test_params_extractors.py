from src.funcs.params_extractors import sample_number_extractor, voltage_extractor, duration_min_extractor, user_extractor, get_mod_date_of_file

class TestSampleNumberExtractor(object):

    def test_with_clean_salt_file(self):
        
        file = "path/to/clean_salt_file.txt"
        
        expected = 20
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_tapwater_file(self):
        
        file = "path/to/clean_tapwater_file.txt"
        
        expected = 20
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = "path/to/empty_file.txt"
        
        expected = None
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = "path/to/random_file.txt"
        
        expected = None
        actual = sample_number_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

class TestVoltageExtractor(object):

    def test_with_clean_salt_file(self):

        file = "path/to/clean_salt_file.txt"
        
        expected = 4.3
        actual = voltage_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_tapwater_file(self):
        
        file = "path/to/clean_tapwater_file.txt"
        
        expected = 8.0
        actual = voltage_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = "path/to/empty_file.txt"
        
        expected = None
        actual = voltage_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = "path/to/random_file.txt"
        
        expected = None
        actual = voltage_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

class TestDurationMinExtractor(object):

    def test_with_clean_salt_file(self):

        file = "path/to/clean_salt_file.txt"
        
        expected = 60
        actual = duration_min_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_tapwater_file(self):
        
        file = "path/to/clean_tapwater_file.txt"
        
        expected = 13
        actual = duration_min_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = "path/to/empty_file.txt"
        
        expected = None
        actual = duration_min_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = "path/to/random_file.txt"
        
        expected = None
        actual = duration_min_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

class TestUserExtractor(object):

    def test_with_clean_salt_file(self):

        file = "path/to/clean_salt_file.txt"
        
        expected = 'BJC'
        actual = user_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_tapwater_file(self):
        
        file = "path/to/clean_tapwater_file.txt"
        
        expected = 'BJC'
        actual = user_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = "path/to/empty_file.txt"
        
        expected = None
        actual = user_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = "path/to/random_file.txt"
        
        expected = None
        actual = user_extractor(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

class TestGetModDateOfFile(object):

    def test_with_clean_salt_file(self):

        file = "path/to/clean_salt_file.txt"
        
        expected = '28-04-2021'
        actual = get_mod_date_of_file(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_tapwater_file(self):
        
        file = "path/to/clean_tapwater_file.txt"
        
        expected = '28-04-2021'
        actual = get_mod_date_of_file(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = "path/to/empty_file.txt"
        
        expected = '10-01-2022'
        actual = get_mod_date_of_file(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = "path/to/random_file.txt"
        
        expected = '12-01-2022'
        actual = get_mod_date_of_file(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message


