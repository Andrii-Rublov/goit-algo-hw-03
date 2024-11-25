from datetime import datetime


# Description: Function calculates the difference between a specified date and the current date.

def get_days_from_today(date):  # Ensure the input is a string in format "%Y-%m-%d"
    try:
        # Converting from string to datetime object
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please provide the date in 'YYYY-MM-DD' format.")

    current_date = datetime.today().date()
    dates_difference = (current_date - parsed_date).days
    print(dates_difference)
    return dates_difference  # Returns the quantity of days, class 'int'


# Test the function
try:
    get_days_from_today("2025-05-25")  # Valid input
    get_days_from_today("2024-05-25")  # Valid input
    get_days_from_today("2024.05.25")  # Invalid input
except ValueError as mistake:
    print(mistake)