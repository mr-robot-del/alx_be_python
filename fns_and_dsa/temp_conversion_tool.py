FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_temperature():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F)? ").strip().upper()
        
        if unit == "C":
            fahrenheit = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
            print(f"{temp}°C is {fahrenheit:.1f}°F")
        elif unit == "F":
            celsius = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
            print(f"{temp}°F is {celsius:.1f}°C")
        else:
            print("Error: Please enter 'C' or 'F' for the unit")
    except ValueError:
        print("Error: Please enter a valid number for the temperature")

if __name__ == "__main__":
    convert_temperature()
