

from datetime import datetime, timedelta

def display_current_datetime():
    
    current_date = datetime.now()
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days_to_add):
    
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Date after {days_to_add} day(s): {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()
    
    try:
        user_input = int(input("Enter the number of days to add: "))
        calculate_future_date(user_input)
    except ValueError:
        print("Please enter a valid integer.")
