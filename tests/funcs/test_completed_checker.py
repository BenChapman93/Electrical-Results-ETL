from src.funcs.completed_checker import TempFile, temp_file_path_generator, completed_checker

class TestCompletedChecker(object):

    def test_with_clean_salt_file(self):
        
        file = "path/to/clean_salt_file.txt"
        
        expected = "path/to/clean_salt_file.txt"
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message  

    def test_with_clean_tapwater_file(self):
        
        file = "path/to/clean_tapwater_file.txt"
        
        expected = "path/to/clean_tapwater_file.txt"
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_empty_file(self):
        
        file = "path/to/empty_file.txt"
        
        expected = None
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_clean_random_file(self):
        
        file = "path/to/clean_random_file.txt"
        
        expected = None
        actual = completed_checker(file)
        message = f"Expected: {expected}, Actual: {actual}"

        assert actual == expected, message

    def test_with_incomplete_file(self):
            
            file = "path/to/incomplete_file.txt"
            
            expected = None
            actual = completed_checker(file)
            message = f"Expected: {expected}, Actual: {actual}"

            assert actual == expected, message  
