import patterns
import re as regex

customer_pattern = regex.compile(patterns.CUSTOMER_TYPE)
date_pattern = regex.compile(patterns.DATES)

def check_reservation_file_entry(line):
    return customer_pattern.match(line.lower()) and date_pattern.search(line)
