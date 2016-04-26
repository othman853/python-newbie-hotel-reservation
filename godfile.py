# This is a god file, no OO, no organization, no tests, just code.
import re as regex

# Compiling a Regex using the raw string python notation (with the preceding r)
# By now, the regex accepts anything
customer_type_pattern = regex.compile(r're(gular|wards)')


def print_file(file):
    line_number = 1
    for line in file:

        # Using match() instead of search() to get the pattern at index 0
        if customer_type_pattern.match(line.lower()):
            print "%d - %s" % (line_number,  line)
        else:
            print 'Invalid entry'

        line_number = line_number + 1

entry_file = open('entries_sample')
print_file(entry_file)
