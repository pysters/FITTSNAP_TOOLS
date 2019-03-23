import unittest
from unittest.mock import Mock

from bmi_calculator.engine import BmiEngine


class TestEngine(unittest.TestCase):

    test_data = {
        'age': 28,
        'gender': 'M',
        'height': 176,
        'height_unit': 'cm',
        'weight': 85,
        'weight_unit': 'kg',
    }

    no_data = {}

    wrong_data = 'wrong_data'

    def test_engine_correct_data(self):
        test_engine = BmiEngine(self.test_data)
        test_engine.start_bmi()
        result = test_engine.get_results()
        self.assertDictEqual(result, result)

    def test_engine_wrong_age(self):
        self. test_data['age']=self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_data)

    def test_engine_wrong_gender(self):
        self. test_data['gender']=self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_data)

    def test_engine_wrong_height(self):
        self. test_data['height']=self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_data)

    def test_engine_wrong_height_unit(self):
        self. test_data['height_unit']=self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_data)

    def test_engine_wrong_weight(self):
        self. test_data['weight']=self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_data)

    def test_engine_wrong_weight_unit(self):
        self. test_data['weight_unit']=self.wrong_data
        with self.assertRaises(ValueError):
            BmiEngine(self.test_data)

    def test_engine_empty_data(self):
        self.test_data.pop('age')
        with self.assertRaises(Exception):
            BmiEngine(self.test_data)


if __name__ == '__main__':
    unittest.main()
