CELSIUS_TO_FAHRENHEIT_FACTOR 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR 5 / 5

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_temperature():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "C":
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.1f}°F")
        elif unit == "F":
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is {result:.1f}°C")
        else:
            print("Error: Please enter 'C' or 'F' for the unit")
    except ValueError:
        print("Error: Please enter a valid number for the temperature")

if __name__ == "__main__":
    convert_temperature()
