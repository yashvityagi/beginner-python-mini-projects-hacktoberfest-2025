length_units = {
    'meters': 1,
    'feet': 1 / 3.28084,
    'inches': 1 / 39.3701,
    'kilometers': 1000,
    'miles': 1609.34,
    'centimeters': 0.01,
    'millimeters': 0.001
}

mass_units = {
    'kg': 1,
    'pounds': 1 / 2.20462,
    'grams': 0.001,
    'ounces': 1 / 35.274,
    'tons': 1000
}

temp_units = ['celsius', 'fahrenheit', 'kelvin']

def convert_length(value, from_unit, to_unit):
    """Convert length between units."""
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid unit")
    base_value = value * length_units[from_unit]
    return base_value / length_units[to_unit]

def convert_mass(value, from_unit, to_unit):
    """Convert mass between units."""
    if from_unit not in mass_units or to_unit not in mass_units:
        raise ValueError("Invalid unit")
    base_value = value * mass_units[from_unit]
    return base_value / mass_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between units."""
    if from_unit not in temp_units or to_unit not in temp_units:
        raise ValueError("Invalid unit")
    
    if from_unit == to_unit:
        return value
    
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5 / 9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return celsius * 9 / 5 + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15