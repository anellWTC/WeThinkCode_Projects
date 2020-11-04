# from mastermind import *
#class Test_create_code(unittest.TestCase):
import unittest
from unittest.mock import patch
from io import StringIO
import mastermind

class TestFunctions(unittest.TestCase):

    @patch("sys.stdin", StringIO("1234\n"))
    def test_answer_input(self):
        self.assertEqual(mastermind.get_answer_input(), "1234")
    
    def test_create_code(self):
        for code in range(100):
            code = mastermind.create_code()

            self.assertNotIn(0, code)
            self.assertNotIn(9, code)
            self.assertEqual(len(code),4)
            # print(code)        
    
    def test_check_correctness(self):
        check = mastermind.check_correctness(12,4)
        self.assertTrue(check == True)
        check = mastermind.check_correctness(10,3)
        self.assertTrue(check == False)
        
    @patch("sys.stdin", StringIO("1432\n5678\n1234\n1628\n"))
    def test_take_turn(self):
        code  = [1,6,2,8]
        test = [(1,1),(2,0),(1,1),(4,0)]
        for i in range(4):
            correct = mastermind.take_turn(code)
            self.assertEqual(str(correct),str(test[i]))
    


if __name__ == '__main__':
    unittest.main()


    