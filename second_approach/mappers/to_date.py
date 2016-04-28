def to_date(date_as_string):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    day = int(date_as_string[0:2])
    month = date_as_string[2:5]
    month_number = months.index(month)
    year = int(date_as_string[5:9])

    return py_date(year, month_number, day)
