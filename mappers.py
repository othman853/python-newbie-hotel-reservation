import patterns
import re as regex
from datetime import date as py_date

from reservation import Reservation

def create_reservation_from_file_entry(file_entry):
    customer_type = regex.compile(patterns.CUSTOMER_TYPE).match(file_entry.lower()).group(0)
    dates_as_string = regex.compile(patterns.DATE).findall(file_entry)
    dates = map(to_date, dates_as_string)

    return Reservation(customer_type, dates)

def to_date(date_as_string):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    day = int(date_as_string[0:2])
    month = date_as_string[2:5]
    month_number = months.index(month)
    year = int(date_as_string[5:9])

    return py_date(year, month_number, day)
