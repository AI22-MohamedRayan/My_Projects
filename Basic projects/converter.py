def get_value():
    while True:
        try:
            value = float(input("Enter a value: "))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_conversion_option():
    print("\nSelect conversion option:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    while True:
        try:
            option = int(input("Enter option number: "))
            if 1 <= option <= 3:
                return option
            else:
                print("Invalid option. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_units():
    print("\nSelect units:")
    print("1. Celsius to Fahrenheit")
    print("2. Meters to Feet")
    print("3. Kilograms to Pounds")
    while True:
        try:
            units = int(input("Enter units number: "))
            if 1 <= units <= 3:
                return units
            else:
                print("Invalid units. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def convert_value(value, units):
    if units == 1:
        # Celsius to Fahrenheit
        return value * 9.0 / 5.0 + 32.0
    elif units == 2:
        # Meters to Feet
        return value * 3.28084
    elif units == 3:
        # Kilograms to Pounds
        return value * 2.20462

def main():
    print("Welcome to the Unit Converter!")
    value = get_value()
    option = get_conversion_option()
    units = get_units()
    converted_value = convert_value(value, units)
    print(f"{value} {get_units_description(option, units)} = {converted_value}")

def get_units_description(option, units):
    if option == 1:
        return "Celsius" if units == 1 else "Fahrenheit"
    elif option == 2:
        return "Meters" if units == 1 else "Feet"
    elif option == 3:
        return "Kilograms" if units == 1 else "Pounds"

if __name__ == "__main__":
    main()
    