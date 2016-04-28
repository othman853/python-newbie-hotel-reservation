import re as regex
from file_processor import FileProcessor

def validate_line(line) :
    customer_type_pattern = regex.compile(r're(gular|wards)')
    return True

processor = FileProcessor('entries_sample')

lines = processor.lines()

valid_lines = filter(validate_line, lines )

print valid_lines
