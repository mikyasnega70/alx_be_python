# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global conversion factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global conversion factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    while True:
        try:
            temp_input = input("Enter the temperature (e.g., 25C, 77F): ").strip().upper()

            if not temp_input:
                raise ValueError("Invalid temperature. Please enter a numeric value followed by C or F.")

            unit = temp_input[-1]
            temperature_str = temp_input[:-1]

            if not temperature_str:
                raise ValueError("Invalid temperature. Please enter a numeric value.")
            
            temperature = float(temperature_str)

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is equal to {converted_temp:.2f}°F")
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is equal to {converted_temp:.2f}°C")
            else:
                print("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
            break # Exit the loop if input is valid
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()