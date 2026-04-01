import numpy as np
import unittest
from pair_programming import feet_inches_to_meters

class test_f2m(unittest.TestCase):

    def test_whole_feet_no_inches(self):
        """6 feet 0 inches should be ~1.8287 meters"""
        self.assertAlmostEqual(feet_inches_to_meters(6, 0), 1.8287, places=3)

    def test_feet_and_inches(self):
        """5 feet 9 inches = 5.75 feet = ~1.7520 meters"""
        self.assertAlmostEqual(feet_inches_to_meters(5, 9), 1.7520, places=3)

    def test_zero_height(self):
        """0 feet 0 inches should be 0.0 meters"""
        self.assertEqual(feet_inches_to_meters(0, 0), 0.0)

    def test_inches_only(self):
        """0 feet 12 inches = 1 foot = ~0.3047 meters"""
        self.assertAlmostEqual(feet_inches_to_meters(0, 12), 0.3047, places=3)

    def test_large_value(self):
        """100 feet 0 inches should be ~30.48 meters"""
        self.assertAlmostEqual(feet_inches_to_meters(100, 0), 30.48, places=1)

if __name__ == "__main__":
    unittest.result = unittest.main(verbosity=2)


# . . No defensive programming
# . . No function, but inputs described
# . . Did not handle rounding, failed one test from rounding discrepancy

# . . Original script took live inputs, well commented
