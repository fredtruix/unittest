import unittest
from employee import Employee


class TestEmpoyee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee("fredrick","trust","50000")
        emp_2 = Employee("john","doe","100000")


        self.assertEqual(emp_1.email, "fredricktrust@gmail.com")
        self.assertEqual(emp_2.email, "johndoe@gmail.com")

        emp_1.first = "orume"
        emp_2.first = "berry"


        self.assertEqual(emp_1.email, "orumetrust@gmail.com")
        self.assertEqual(emp_2.email, "berrydoe@gmail.com")


    def test_fullname(self):
        emp_1 = Employee("fredrick","trust","50000")
        emp_2 = Employee("john","doe","100000")

        self.assertEqual(emp_1.fullname, "fredrick trust")
        self.assertEqual(emp_2.fullname, "john doe")


        emp_1.first = "orume"
        emp_2.first = "berry"

        self.assertEqual(emp_1.fullname, "orume trust")
        self.assertEqual(emp_2.fullname, "berry doe")






if __name__ == '__main__':
    unittest.main()