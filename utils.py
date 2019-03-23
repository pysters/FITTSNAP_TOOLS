import re
import inflect

from settings import (UNIT_FEET, WEIGHT_UNITS, HEIGHT_UNITS, GENDERS, AGE_LIMIT,
                      ACCEPTED_GENDERS, ACCEPTED_WEIGHT_UNITS, ACCEPTED_HEIGHT_UNITS)

NUMBER_ONLY_INPUT = 'NUMBER_ONLY_INPUT'
NUMBER_WITH_SPACE_DOT_INPUT = 'NUMBER_WITH_SPACE_DOT_INPUT'
GENDER_INPUT = 'GENDER_INPUT'
NUMERIC_ONLY_REGEX_PATTERN = r'\d*[.]\d*$|\d*$'
NUMERIC_WITH_SPACE_DOT_REGEX_PATTERN = r'\d*[. ]\d*$|\d*$'
GENDER_REGEX_PATTERN = r'^[a-z]$|^[A-Z]$'
INPUT_VALIDATORS = {
    NUMBER_ONLY_INPUT: re.compile(NUMERIC_ONLY_REGEX_PATTERN, re.UNICODE),
    NUMBER_WITH_SPACE_DOT_INPUT: re.compile(NUMERIC_WITH_SPACE_DOT_REGEX_PATTERN, re.UNICODE),
    GENDER_INPUT: re.compile(GENDER_REGEX_PATTERN, re.UNICODE)
}

UNIT = inflect.engine()

USER_INPUT_TEMPLATES = {
    'get_weight_unit': {'template': 'SELECT WEIGHT UNIT: Press {}:',
                        'params': ACCEPTED_WEIGHT_UNITS},
    'get_weight': {'template': 'ENTER WEIGHT: in {}:',
                   'params': WEIGHT_UNITS},
    'get_height_unit': {'template': 'SELECT HEIGHT UNIT: Press {}:',
                        'params': ACCEPTED_HEIGHT_UNITS},
    'get_height': {'template': 'ENTER HEIGHT: in {} :',
                   'params': HEIGHT_UNITS},
    'get_age': {'template': 'ENTER AGE (>{}):',
                'params': AGE_LIMIT},
    'get_gender': {'template': 'ENTER GENDER: Press {}:',
                   'params': GENDERS}
}


class UnitConverter:
    def __init__(self):
        pass

    def feet_to_inch(self, feet, inch):
        return feet * 12 + inch

    def cm_to_inch(self, height_in_cm):
        return height_in_cm / 2.54

    def inch_to_cm(self, height_in_inch):
        return height_in_inch * 2.54

    def cm_to_meter(self, height_in_cm):
        return height_in_cm * 0.01

    def kg_to_lb(self, kg):
        return kg * 2.20462

    def lb_to_kg(self, lb):
        return lb / 2.20462


class UserInput:
    convert = UnitConverter()

    def __init__(self):
        pass

    def _validate_input_recieved(self, _input, validator):
        if not INPUT_VALIDATORS[validator].match(str(_input)):
            raise ValueError('Invalid Input: {} validation failed'.format(validator))

    def _get_user_input(self, data_received=None, validator=None, label=None, display_unit=None):
        if label:
            if display_unit:
                dynamic_text = self.pluralize(
                    USER_INPUT_TEMPLATES[label].get('params').get(display_unit)
                )
            else:
                dynamic_text = USER_INPUT_TEMPLATES[label].get('params')
            interface_text = USER_INPUT_TEMPLATES[label].get('template').format(
                dynamic_text
            )
            print(interface_text, flush=True)

        if not data_received:
            data_received = input()

        if validator:
            self._validate_input_recieved(data_received, validator)
        return str(data_received).upper()

    def pluralize(self, measurement_unit):
        return UNIT.plural(measurement_unit)

    def get_gender(self, data_received=None):
        gender_received = self._get_user_input(data_received=data_received,
                                               validator=GENDER_INPUT,
                                               label='get_gender')
        if gender_received in ACCEPTED_GENDERS:
            return gender_received
        else:
            raise ValueError('Gender must be either of {}'.format(ACCEPTED_GENDERS))

    def get_age(self, data_received=None):
        age_received = float(self._get_user_input(data_received=data_received,
                                                  validator=NUMBER_ONLY_INPUT,
                                                  label='get_age'))
        if age_received > AGE_LIMIT:
            return age_received
        else:
            raise ValueError('Unsupported age category : currently supports only for adults whose age > 20')

    def get_height(self, height_value=None, height_unit=None):
        height_unit = self._get_user_input(data_received=height_unit,
                                           label='get_height_unit')
        if height_unit in ACCEPTED_HEIGHT_UNITS:
            height_value = self._get_user_input(data_received=height_value,
                                                validator=NUMBER_WITH_SPACE_DOT_INPUT,
                                                label='get_height',
                                                display_unit=height_unit)
            if height_unit in UNIT_FEET:
                return str(height_value), height_unit
            else:
                return float(height_value), height_unit
        else:
            raise ValueError('Height units must be either of {}'.format(ACCEPTED_HEIGHT_UNITS))

    def get_weight(self, weight_value=None, weight_unit=None):
        weight_unit = self._get_user_input(data_received=weight_unit,
                                           label='get_weight_unit')

        if weight_unit in ACCEPTED_WEIGHT_UNITS:
            weight_value = float(self._get_user_input(data_received=weight_value,
                                                      validator=NUMBER_ONLY_INPUT,
                                                      label='get_weight',
                                                      display_unit=weight_unit))
            return weight_value, weight_unit
        else:
            raise ValueError('Weight units must be either of {}'.format(ACCEPTED_WEIGHT_UNITS))
