import unittest
import  calc
#  python3 -m unittest test_calc.py

class TestCalc(unittest.TestCase):

# all test need to start with the word "test" by convention and with "_" and the function name in this example "add"
    def test_add(self):
        # we are using the assertEqual tool from unittest
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)


    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)

    

if __name__ == '__main__':
    unittest.main()