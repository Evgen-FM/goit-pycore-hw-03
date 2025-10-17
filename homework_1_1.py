from datetime import datetime

def get_days_from_today(date):

    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None
    today = datetime.today()
    count_days = today - date_obj
    return count_days.days

print(get_days_from_today("2026-11-09"))

