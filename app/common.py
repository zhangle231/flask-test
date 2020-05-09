import time,datetime

def parse_date(date_str):
    fmt = '%Y-%m-%d'
    time_tuple = time.strptime(date_str, fmt)
    year, month, day = time_tuple[:3]
    new_date = datetime.date(year, month, day)
    return new_date
