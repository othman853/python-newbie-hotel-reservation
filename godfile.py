# This is a god file, no OO, no organization, no tests, just code.
import re as regex

# Compiling a Regex using the raw string python notation (with the preceding r)
# By now, the regex accepts anything
reservation_pattern = regex.compile(r'.')

def format_line(line_number, line):
    return

def print_file(file):
    line_number = 1
    for line in file:
        print "%d - %s" % (line_number,  line)
        line_number = line_number + 1

entry_file = open('entries_sample')
print_file(entry_file)
