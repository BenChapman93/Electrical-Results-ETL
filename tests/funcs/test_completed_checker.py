from src.funcs.completed_checker import TempFile, temp_file_path_generator, completed_checker

class TestCompletedChecker(object):

    def test_with_clean_salt_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 1 HRS SALTBJC.txt"
        
        expected = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 1 HRS SALTBJC.txt"
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message  

    def test_with_clean_tapwater_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 13 MIN TAPBJC.txt"
        
        expected = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 13 MIN TAPBJC.txt"
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\empty_file.txt"
        
        expected = None
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\random_text.txt"
        
        expected = None
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_incomplete_file(self):
            
            file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\incomplete_file.txt"
            
            expected = None
            actual = completed_checker(file)
            message = f"Expected: {expected}, Actual: {actual}"

            assert actual == expected, message  