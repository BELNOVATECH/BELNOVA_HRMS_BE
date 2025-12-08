from datetime import datetime, date
from typing import Union

def convert_date(value: Union[str, date, None]) -> date | None:
    """
    Convert a string to a date object.
    Accepts formats: DD-MM-YYYY, YYYY-MM-DD.
    Returns date as-is if already a date object.
    """
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if not isinstance(value, str):
        raise ValueError(f"Invalid type for date conversion: {type(value)}")

    for fmt in ("%d-%m-%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Invalid date format. Expected DD-MM-YYYY or YYYY-MM-DD, got '{value}'")


def convert_datetime(value: Union[str, datetime, None]) -> datetime | None:
    """
    Convert a string to a datetime object.
    Accepts formats: DD-MM-YYYY HH:MM:SS, YYYY-MM-DD HH:MM:SS.
    Returns datetime as-is if already a datetime object.
    """
    if value is None:
        return None
    if isinstance(value, datetime):
        return value
    if not isinstance(value, str):
        raise ValueError(f"Invalid type for datetime conversion: {type(value)}")

    for fmt in ("%d-%m-%Y %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise ValueError(
        f"Invalid datetime format. Expected DD-MM-YYYY HH:MM:SS or YYYY-MM-DD HH:MM:SS, got '{value}'"
    )
