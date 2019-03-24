import unittest

from bmi_calculator.engine import BmiEngine, InvalidInputError


class TestEngineInputs(unittest.TestCase):

    def setUp(self):
        self.test_data = {
            'age': 28,
            'gender': 'M',
            'height': 176,
            'height_unit': 'cm',
            'weight': 85,
            'weight_unit': 'kg',
        }
        self.test_missing_data = self.test_data
        self.test_wrong_data = self.test_data
        self.no_data = {}
        self.wrong_data = 'wrong_data'

    def test_engine_wrong_age(self):
        self.test_wrong_data['age'] = self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_wrong_data)

    def test_engine_wrong_gender(self):
        self.test_wrong_data['gender'] = self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_wrong_data)

    def test_engine_wrong_height(self):
        self.test_wrong_data['height'] = self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_wrong_data)

    def test_engine_wrong_height_unit(self):
        self.test_wrong_data['height_unit'] = self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_wrong_data)

    def test_engine_wrong_weight(self):
        self.test_wrong_data['weight'] = self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_wrong_data)

    def test_engine_wrong_weight_unit(self):
        self.test_wrong_data['weight_unit'] = self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_wrong_data)

    def test_engine_missing_age_data(self):
        self.test_missing_data.pop('age')
        with self.assertRaises(InvalidInputError):
            BmiEngine(self.test_missing_data)

    def test_engine_missing_gender_data(self):
        self.test_missing_data.pop('gender')
        with self.assertRaises(InvalidInputError):
            BmiEngine(self.test_missing_data)

    def test_engine_missing_weight_data(self):
        self.test_missing_data.pop('weight')
        with self.assertRaises(InvalidInputError):
            BmiEngine(self.test_missing_data)

    def test_engine_missing_weight_unit_data(self):
        self.test_missing_data.pop('weight_unit')
        with self.assertRaises(InvalidInputError):
            BmiEngine(self.test_missing_data)

    def test_engine_missing_height_data(self):
        self.test_missing_data.pop('height')
        with self.assertRaises(InvalidInputError):
            BmiEngine(self.test_missing_data)

    def test_engine_missing_height_unit_data(self):
        self.test_missing_data.pop('height_unit')
        with self.assertRaises(InvalidInputError):
            BmiEngine(self.test_missing_data)


if __name__ == '__main__':
    unittest.main()
