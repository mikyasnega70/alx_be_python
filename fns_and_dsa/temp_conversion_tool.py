
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
   
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
   
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    try:
        temp_input = input("Enter the temperature value: ")
        temp_value = float(temp_input)

        unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            converted = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is {converted:.2f}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is {converted:.2f}°C")
        else:
            raise ValueError("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            
    except ValueError as e:
        print(f"Invalid temperature. {e}")
