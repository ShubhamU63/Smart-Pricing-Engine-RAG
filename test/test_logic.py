# tests/test_logic.py

import unittest
from rag.labor_calc import calculate_labor_cost
from rag.vat_rules import get_vat_rate

class TestPricingLogic(unittest.TestCase):

    def test_calculate_labor_cost(self):
        self.assertEqual(calculate_labor_cost(10, 50), 500.00)
        self.assertEqual(calculate_labor_cost(0, 50), 0.00)
        with self.assertRaises(ValueError):
            calculate_labor_cost(-5, 50)

    def test_get_vat_rate(self):
        self.assertEqual(get_vat_rate("FR"), 0.20)
        self.assertEqual(get_vat_rate("UK"), 0.20)
        self.assertEqual(get_vat_rate("XX"), 0.20)  # default

if __name__ == "__main__":
    unittest.main()
