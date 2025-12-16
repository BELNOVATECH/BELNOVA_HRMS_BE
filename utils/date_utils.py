from datetime import datetime, date

# Convert "DD-MM-YYYY" → date object
def convert_date(value: str) -> date:
    """
    Converts string in format DD-MM-YYYY or YYYY-MM-DD to Python date object.
    """
    try:
        # Try DD-MM-YYYY
        return datetime.strptime(value, "%d-%m-%Y").date()
    except ValueError:
        pass

    try:
        # Try YYYY-MM-DD
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date format must be DD-MM-YYYY or YYYY-MM-DD")


# Convert "DD-MM-YYYY HH:MM" → datetime object
def convert_datetime(value: str) -> datetime:
    """
    Converts string in format DD-MM-YYYY HH:MM or YYYY-MM-DD HH:MM to Python datetime object.
    """
    try:
        return datetime.strptime(value, "%d-%m-%Y %H:%M")
    except ValueError:
        pass

    try:
        return datetime.strptime(value, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Datetime format must be DD-MM-YYYY HH:MM or YYYY-MM-DD HH:MM")
