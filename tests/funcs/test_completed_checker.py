from src.funcs.completed_checker import TempFile, temp_file_path_generator, completed_checker

class TestCompletedChecker(object):

    def test_with_clean_salt_file(self):
        
        file = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 1 HRS SALTBJC.txt"
        
        expected = r"C:\Users\ben.chapman\Desktop\Udemy\Electrical_Results_ETL\mock_files\Complete 1 HRS SALTBJC.txt"
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message    