from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")

def to_ist(dt):
    if not dt:
        return None
    return dt.astimezone(IST).strftime("%Y-%m-%d %I:%M %p")
