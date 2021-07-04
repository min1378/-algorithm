def is_backup(query):
    if (query[-1] == '~'):
        return True
    return False


def is_under_size(size):
    unit = size[-1]
    if (unit == 'G'): return False
    if (unit == 'M'):
        number = int(size[:-1])
        if (number >= 14): return False
    return True


def is_last_date(date):
    [year, month, day] = date.split("-")
    rest = (int(year) - 1990) * 365 + (int(month) - 1) * 30 + int(day) - 31
    if (rest <= 0): return False
    return True


def solution(S):
    querys = S.strip().split("\n")
    result = 100000000
    for query in querys:
        new_query = query.strip()
        if (not is_backup(new_query)):
            continue
        [size, date, file] = new_query.split(" ")
        if (not is_under_size(size)):
            continue
        if (not is_last_date(date)):
            continue
        [name, extension] = file.split(".")
        result = min(len(name), result)
    if (result == 100000000):
        return "NO FILES"
    return result


solution(
    ' 715K 2009-09-23 system.zip~\n 179K 2013-08-14 to-do-list.xml~\n 645K 2013-06-19 blockbuster.mpeg~\n  536 2010-12-12 notes.html\n 688M 1990-02-11 delete-this.zip~\n  23K 1987-05-24 setup.png~\n 616M 1965-06-06 important.html\n  14M 1992-05-31 crucial-module.java~\n 192K 1990-01-31 very-long-filename.dll~'
)
