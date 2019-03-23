AGE_LIMIT = 20

GENDER_MALE = ('M', 'MALE')
GENDER_FEMALE = ('F', 'FEMALE')
GENDERS = {
    GENDER_MALE[0]: GENDER_MALE[1],
    GENDER_FEMALE[0]: GENDER_FEMALE[1],
}
ACCEPTED_GENDERS = tuple(GENDERS.keys())

# Height Measure Units
UNIT_FEET = ('FT', 'FEET-INCH')
UNIT_CENTIMETER = ('CM', 'CENTIMETER')
UNIT_METER = ('M', 'METER')

HEIGHT_UNITS = {
    UNIT_FEET[0]: UNIT_FEET[1],
    UNIT_CENTIMETER[0]: UNIT_CENTIMETER[1],
    UNIT_METER[0]: UNIT_METER[1],
}
ACCEPTED_HEIGHT_UNITS = tuple(HEIGHT_UNITS.keys())

# Weight Measure Units
UNIT_POUND = ('LB', 'POUND')
UNIT_KILOGRAM = ('KG', 'KILO-GRAM')
WEIGHT_UNITS = {
    UNIT_POUND[0]: UNIT_POUND[1],
    UNIT_KILOGRAM[0]: UNIT_KILOGRAM[1],
}
ACCEPTED_WEIGHT_UNITS = tuple(WEIGHT_UNITS.keys())

# Body fat chart
BODY_FAT_PERCENTAGE_CHART = {
    GENDER_MALE[0]: [25, (18, 25), (14, 17), (6, 13)],
    GENDER_FEMALE[0]: [31, (25, 31), (21, 24), (14, 20)]
}

# Body mass index chart
BMI_CHART = [15.0, 16.0, 18.5, 25.0, 30.0, 35.0, 40.0, 40.0]