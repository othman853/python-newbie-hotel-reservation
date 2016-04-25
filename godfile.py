# This is a god file, no OO, no organization, no tests, just code.
def print_file(file):
    line_number = 1
    for line in file:
        print "%d - %s" % (line_number,  line)
        line_number = line_number + 1



entry_file = open('entries_sample')
print_file(entry_file)
