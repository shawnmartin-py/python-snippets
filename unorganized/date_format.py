from datetime import datetime, timedelta, timezone
import calendar
import re


CST = timezone(-timedelta(hours=6), name="CST")
ts = datetime.now()


def replace_code(mo):
    c = mo.group(1)
    match c:
        case "a": return calendar.day_abbr[ts.weekday()]
        case "A": return calendar.day_name[ts.weekday()]
        case "w": return str(ts.weekday())
        case "d": return f"{ts.day:02d}"
        case "b": return calendar.month_abbr[ts.month]
        case "B": return calendar.month_name[ts.month]
        case "m": return f"{ts.month:02d}"
        case "y": return f"{ts.year % 100:02d}"
        case "Y": return f"{ts.year:04d}"
        case "H": return f"{ts.hour:02d}"
        case "I": return f"{ts.hour % 12:02d}"
        case "p": return "PM" if ts.hour > 12 else "AM"
        case "M": return f"{ts.minute:02d}"
        case "S": return f"{ts.second:02d}"
        case "f": return f"{ts.microsecond:06d}"
        case "j": return f"{ts.timetuple().tm_yday:03d}"
        case "%": return "%"
        case _: raise ValueError(f"Unknown code: {c}")

def date_format(datestr):
    return re.sub(r"%([A-Za-z])", replace_code, datestr)

