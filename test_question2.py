import unittest
import unittest.mock
import random
import io
from  solution.question2 import *

# stdout object
mock_stdout = unittest.mock.patch('sys.stdout', new_callable=io.StringIO)

class TestQuestion(unittest.TestCase):
    
    @mock_stdout
    def test_case1(self,stdout):  
        #test data
        person_a = Person("User", "1", None)
        person_b = Person("User", "2", person_a) 
        test_data = {
        "key1": 1,
        "key2": {
        "key3": 1,
        "key4": {
        "key5": 4,
        "user": person_b,
        }
        }
        }
        expected_output = "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser 3\nfirst_name 4\nlast_name 4\nfather 4\nfirst_name 5\nlast_name 5\nfather 5\n"
        print_depth(test_data)
        capturedOutput = stdout.getvalue()
        self.assertEqual(capturedOutput, expected_output)


    def test_type(self):
        
        with self.assertRaises(TypeError):
            print_depth([33,4,5,1])
        
        with self.assertRaises(TypeError):
            print_depth('test')

        with self.assertRaises(TypeError):
            print_depth(None)





if __name__=='__main__':
    unittest.main()