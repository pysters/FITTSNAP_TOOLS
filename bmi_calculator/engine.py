from bmi_calculator.calculator import Bmi, BmiCategory
from bmi_calculator.utils import UserInput

REQUIRED_PARAMS = set(['age', 'gender', 'height',
                       'height_unit', 'weight', 'weight_unit'])


class InvalidInputError(ValueError):
    pass


class BmiEngine:
    age = None
    gender = None
    height = None
    weight = None
    height_unit = None
    weight_unit = None

    bmi_ = None
    bmi_category = None
    bfp = None
    bfp_category = None
    recommended_weight = None

    bmi = Bmi()
    input = UserInput()
    category = BmiCategory()

    def __init__(self, data=dict()):
        if data and self.validate_input_data(data):
            self.get_or_set_required_input(data)
        else:
            self.get_or_set_required_input()

    def validate_input_data(self, data=dict()):
        data_keys = set(data.keys())
        if data_keys == REQUIRED_PARAMS:
            return True
        else:
            missing_data = REQUIRED_PARAMS - data_keys
            raise InvalidInputError(
                'Invalid Data : Missing required data :{} values'.format(
                    missing_data
                ))

    def get_or_set_required_input(self, data=dict()):
        self.gender = self.input.get_gender(data.get('gender'))
        self.age = self.input.get_age(data.get('age'))
        self.height, self.height_unit = self.input.get_height(data.get('height'),
                                                              data.get('height_unit'))
        self.weight, self.weight_unit = self.input.get_weight(data.get('weight'),
                                                              data.get('weight_unit'))

    def start_bmi(self):
        self.bmi_, self.bmi_category = self.bmi.calculate_bmi(self.height,
                                                              self.height_unit,
                                                              self.weight,
                                                              self.weight_unit)
        self.recommended_weight = self.bmi.recommend_weight(self.height,
                                                            self.height_unit)
        self.bfp = self.bmi.body_fat_percent(_gender=self.gender,
                                             _bmi=self.bmi_, _age=self.age)
        self.bfp_category = self.bmi.body_fat_category(_bfp=self.bfp,
                                                       _gender=self.gender)

    def display_results(self):
        print()
        print('-'*89)
        print('BMI & Stats')
        print("Height : {} {}, Weight: {} {}, Age:{}, Sex:{}".format(
            self.height, self.input.pluralize(self.height_unit),
            self.weight, self.input.pluralize(self.weight_unit),
            self.age, self.gender
        ))
        print('-'*89)
        print("Your BMI: {} KG/M^2".format(self.bmi_))
        print("Your BMI category: {}".format(self.bmi_category))
        print("Weight Range: Min - {} {} Max - {} {}".format(self.recommended_weight[0],
                                                             self.input.pluralize(
                                                                 self.weight_unit),
                                                             self.recommended_weight[1],
                                                             self.input.pluralize(
                                                                 self.weight_unit)
                                                             ))
        print("Body Fat Percentage: {} %".format(self.bfp))
        print("Body Fat Percentage Category: {}".format(self.bfp_category))
        print('-'*89)

    def get_results(self):
        bmi_results = {
            'age': self.age,
            'gender': self.gender,
            'height': self.height,
            'height_unit': self.input.pluralize(self.height_unit),
            'weight': self.weight,
            'weight_unit': self.input.pluralize(self.weight_unit),
            'weight_range': self.recommended_weight,
            'body_mass_index': self.bmi_,
            'body_mass_index_category': self.bmi_category,
            'body_fat_percentage': self.bfp,
            'boday_fat_percentage_category': self.bfp_category,
        }
        return bmi_results


if __name__ == '__main__':

    test_data = {
        'gender': 'M',
        'height': 176,
        'height_unit': 'cm',
        'weight': 85,
        'weight_unit': 'kg',
    }

    bmi_engine = BmiEngine(test_data)
    bmi_engine.start_bmi()
    bmi_engine.display_results()
    bmi_engine.get_results()
