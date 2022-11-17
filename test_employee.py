import unittest
from employee import Employee


class TestEmpoyee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee("fredrick","trust","50000")
        emp_2 = Employee("John","doe","100000")


        self.assertEqual(emp_1.email, "fredricktrust@gmail.com")
        self.assertEqual(emp_2.email, "Johndoe@gmail.com")

        emp_1.first = "orume"
        emp_2.first = "berry"


        self.assertEqual(emp_1.email, "orumetrust@gmail.com")
        self.assertEqual(emp_2.email, "berrydoe@gmail.com")








if __name__ == '__main__':
    unittest.main()