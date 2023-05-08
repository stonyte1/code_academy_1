import unittest
from loan_calculator import Loan

class TestMyClass(unittest.TestCase):
    def setUp(self):
        self.obj = Loan(2000, 30, 1.2)

    def test_add(self):
        self.assertEqual(self.obj.month_interest_rate, 60.0)
        self.assertEqual(self.obj.month_sum_increase, 2030.0)

if __name__ == '__main__':
    unittest.main()