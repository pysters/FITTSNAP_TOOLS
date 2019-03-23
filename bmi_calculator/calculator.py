from bmi_calculator.utils import UnitConverter
from bmi_calculator.settings import (GENDER_FEMALE, GENDER_MALE, UNIT_FEET, UNIT_METER,
                                     UNIT_CENTIMETER, UNIT_KILOGRAM, UNIT_POUND,
                                     BODY_FAT_PERCENTAGE_CHART, BMI_CHART)


class BmiCategory:

    def __init__(self):
        pass

    def bmi_category(self, bmi):
        if bmi < BMI_CHART[0]:
            return 'Very severely underweight'
        elif bmi < BMI_CHART[1]:
            return 'Severely underweight'
        elif bmi < BMI_CHART[2]:
            return 'Underweight'
        elif bmi < BMI_CHART[3]:
            return 'Great shape!'
        elif bmi < BMI_CHART[4]:
            return 'Overweight'
        elif bmi < BMI_CHART[5]:
            return 'Obese Class I Moderately obese'
        elif bmi <= BMI_CHART[6]:
            return 'Obese Class II Severely obese'
        elif bmi > BMI_CHART[7]:
            return 'Very severely obese'

    def body_fat_percentage_category(self, bfp, gender):
        get_body_fat_percentage_chart = BODY_FAT_PERCENTAGE_CHART.get(gender[0])
        if get_body_fat_percentage_chart:
            if bfp > get_body_fat_percentage_chart[0]:
                return "Obese"
            elif get_body_fat_percentage_chart[1][0] <= bfp <= get_body_fat_percentage_chart[1][1]:
                return "Acceptable"
            elif get_body_fat_percentage_chart[2][0] <= bfp <= get_body_fat_percentage_chart[2][1]:
                return "Fitness"
            elif get_body_fat_percentage_chart[3][0] <= bfp <= get_body_fat_percentage_chart[3][1]:
                return "Athletes"
            else:
                return "Essential Fat"
        else:
            raise ValueError("Gender must be M (Male) or F(Female)")


class Bmi:
    convert = UnitConverter()
    category = BmiCategory()

    def __init__(self):
        pass

    def body_fat_percent(self, _gender, _bmi, _age):
        # Adult Body Fat % = (1.20 x BMI) + (0.23 x Age) – (10.8 x gender) – 5.4
        # using gender male = 1, female = 0.
        if _gender[0] == GENDER_MALE[0]:
            return round(((1.20 * _bmi) + (0.23 * _age) - 10.8 - 5.4), 1)
        elif _gender[0] == GENDER_FEMALE[0]:
            return round(((1.20 * _bmi) + (0.23 * _age) - 5.4), 1)

    def recommend_weight(self, height, unit):
        weight_range = []
        height_in_meter = self.convert_to_meter(height, unit)
        weight_range.append(round((18.5 * (height_in_meter * height_in_meter)), 1))
        weight_range.append(round((25 * (height_in_meter * height_in_meter)), 1))
        return weight_range

    def convert_to_meter(self, height, unit):
        if unit == UNIT_FEET[0]:
            if '.' in str(height):
                inp = str(height).split('.')
            else:
                inp = str(height).split()

            if '' in inp:
                inp.remove('')

            if len(inp) < 2:
                inp.append('0')

            height_in_inch = self.convert.feet_to_inch(float(inp[0]), float(inp[1]))
            height_in_cm = self.convert.inch_to_cm(height_in_inch)
            height_in_meter = self.convert.cm_to_meter(height_in_cm)
            return height_in_meter
        elif unit == UNIT_METER[0]:
            return height
        elif unit == UNIT_CENTIMETER[0]:
            height_in_meter = self.convert.cm_to_meter(height)
            return height_in_meter

    def convert_to_kg(self, weight, unit):
        if unit == UNIT_KILOGRAM[0]:
            return weight
        if unit == UNIT_POUND[0]:
            weight_in_kg = self.convert.lb_to_kg(weight)
            return weight_in_kg

    def calculate_bmi(self, height, height_unit, weight, weight_unit):
        height_in_meter = self.convert_to_meter(height, height_unit)
        weight_in_kg = self.convert_to_kg(weight, weight_unit)
        bmi = round((weight_in_kg/(height_in_meter * height_in_meter)), 1)
        category = self.category.bmi_category(bmi)
        return bmi, category

    def body_fat_category(self, _bfp, _gender):
        return self.category.body_fat_percentage_category(bfp=_bfp, gender=_gender)
