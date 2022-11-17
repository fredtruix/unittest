import unittest
from employee import Employee


class TestEmpoyee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee("fredrick","trust",50000)
        self.emp_2 = Employee("john","doe",10000)

    def tearDown(self):
        pass

    def test_email(self):
    
        self.assertEqual(self.emp_1.email, "fredricktrust@gmail.com")
        self.assertEqual(self.emp_2.email, "johndoe@gmail.com")

        self.emp_1.first = "orume"
        self.emp_2.first = "berry"


        self.assertEqual(self.emp_1.email, "orumetrust@gmail.com")
        self.assertEqual(self.emp_2.email, "berrydoe@gmail.com")


    def test_fullname(self):
      

        self.assertEqual(self.emp_1.fullname, "fredrick trust")
        self.assertEqual(self.emp_2.fullname, "john doe")


        self.emp_1.first = "orume"
        self.emp_2.first = "berry"

        self.assertEqual(self.emp_1.fullname, "orume trust")
        self.assertEqual(self.emp_2.fullname, "berry doe")


    def test_apply_raise(self):

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 10500)





if __name__ == '__main__':
    unittest.main()