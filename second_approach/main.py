from readers.file_processor import FileProcessor
from filters.check_reservation_file_entry import check_reservation_file_entry as is_reservation_valid
from mappers.create_reservation_from_file_entry import create_reservation_from_file_entry as to_reservation

processor = FileProcessor('entries_sample')

entries = processor.filtered_lines(is_reservation_valid)

reservations = map(to_reservation, entries)

for reservation in reservations:
    print reservation.customer_type
    print reservation.dates
