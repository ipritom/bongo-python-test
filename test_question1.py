import unittest
import unittest.mock
import random
import io
from solution import question1

# stdout object
mock_stdout = unittest.mock.patch('sys.stdout', new_callable=io.StringIO)

class TestQuestion(unittest.TestCase):
    
    @mock_stdout
    def test_case1(self,stdout):   
        test_data = {
            "key1": 1,
            "key2": {
            "key3": 1,
            "key4": {
            "key5": 4
            }
            }
            }
        expected_output = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n" 
        question1.print_depth(test_data)
        capturedOutput = stdout.getvalue()
        self.assertEqual(capturedOutput, expected_output)

    def test_type(self):
        '''
        Input: Unexpected Datatype
        '''
        
        with self.assertRaises(TypeError):
            question1.print_depth([33,4,5,1])
        
        with self.assertRaises(TypeError):
            question1.print_depth('test')

        with self.assertRaises(TypeError):
            question1.print_depth(None)





if __name__=='__main__':
    unittest.main()