def is_last_date(date):
    [year, month, day] = date.split("-")
    rest = (int(year) - 1990) * 365 + (int(month) - 1) * 30 + int(day) - 31
    if (rest <= 0): return False
    return True


print(is_last_date('1991-01-32'))