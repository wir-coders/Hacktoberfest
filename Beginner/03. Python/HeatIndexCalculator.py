import math

def _convert_to_fahrenheit(celcius):
    fahrenheit = (celcius * 1.8) + 32
    return fahrenheit


def _convert_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) / 1.8
    return celcius


def _get_dew_point(temperature_celcius, humidity_percent):
    r = ((17.27 * temperature_celcius) / (237.1 + temperature_celcius)) + math.log((humidity_percent/100))
    
    dew_point = (237.1 * r) / (17.27 - r)
    print(round(dew_point, 4))


def _complete_heat_index(temperature_fahrenheit, humidity_percent):

    F = temperature_fahrenheit
    H = humidity_percent
    heat_index = -42.379  + (2.04901523 * F) + (10.14333127 * H) + (-0.22475541 * F * H) +\
        (-0.00683783 * F * F) + (-0.05481717 * H * H) + (0.00122874 * F * F * H) + (0.00085282 * F * H * H ) + (-0.00000199 * F * F * H * H)

    if humidity_percent < 13 and F >= 80 and F <= 113:
        correction = ((13 - H) / 4) * math.sqrt(17 - abs(F - 95) / 17)
        return heat_index - correction
    
    if H > 85 and F >= 80 and F <= 87:
        correction = ((H - 85) / 10) * ((87 - F) /5)
        return heat_index - correction

    if heat_index < 80:
        heat_index = 0.5 * (F + 61 + ((F - 68) * 1.2) + (H * 0.094))
        return heat_index

    return heat_index


def _simple_heat_index(temperature_fahrenheit, humidity_percent):
    F = temperature_fahrenheit
    H = humidity_percent

    HI = 1.1 * F + 0.047 * H - 10.3
    return HI


def calculate_heat_index(temperature_celcius, humidity_percent):
    F = _convert_to_fahrenheit(temperature_celcius)
    H = humidity_percent

    HI = _simple_heat_index(F, H)

    if HI >= 80:
        # Use the complete version
        HI = _complete_heat_index(F, H)

    return round(_convert_to_celcius(HI), 4)


print(calculate_heat_index(17, 56))