import re as regex
from filters import check_reservation_file_entry as is_reservation_valid
from file_processor import FileProcessor

processor = FileProcessor('entries_sample')

print processor.filtered_lines(is_reservation_valid)
