import unittest
from unittest.mock import patch
from employee import Employee


class TestEmpoyee(unittest.TestCase):


    #  setupclass run @ the bigining before any  test
    @classmethod
    def setUpClass(cls) -> None:
        print('setupclass')

    # teardownclass run @ the end of the all the test
    @classmethod
    def tearDownClass(cls) -> None:
        print('teardownclass')


    #  setup run @ the bigining of every test
    def setUp(self):
        print('setUp')
        self.emp_1 = Employee("fredrick","trust",50000)
        self.emp_2 = Employee("john","doe",10000)

    #  teardown run out the end of every test
    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, "fredricktrust@gmail.com")
        self.assertEqual(self.emp_2.email, "johndoe@gmail.com")

        self.emp_1.first = "orume"
        self.emp_2.first = "berry"


        self.assertEqual(self.emp_1.email, "orumetrust@gmail.com")
        self.assertEqual(self.emp_2.email, "berrydoe@gmail.com")


    def test_fullname(self):
        print('test_fullname')

        self.assertEqual(self.emp_1.fullname, "fredrick trust")
        self.assertEqual(self.emp_2.fullname, "john doe")


        self.emp_1.first = "orume"
        self.emp_2.first = "berry"

        self.assertEqual(self.emp_1.fullname, "orume trust")
        self.assertEqual(self.emp_2.fullname, "berry doe")


    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 10500)

    def test_monthly_schedule(self):

        with patch('employee.requests.get') as mocked_get:

            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
           

            schedule = self.emp_1.monthly_schedule("May")
            mocked_get.assert_called_with('http://company.com/trust/May')
            self.assertEqual(schedule, 'Success')



            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            print(schedule)
            mocked_get.assert_called_with("http://company.com/doe/June")
            self.assertEqual(schedule, 'Bad Response!')

            





if __name__ == '__main__':
    unittest.main()