import unittest

from bmi_calculator.utils import UnitConverter


class TestEngine(unittest.TestCase):

    def setUp(self):
        test_value = 4.0
        self.feets = test_value
        self.cms = test_value
        self.mts = test_value
        self.inches = test_value
        self.lbs = test_value
        self.kgs = test_value

        self.feet2inch_expected = 48.0

        self.convert = UnitConverter()

    def test_feet_to_inches(self):
        obtained_result = self.convert.feet2inch(feet=self.feets)
        assert obtained_result == self.feet2inch_expected

