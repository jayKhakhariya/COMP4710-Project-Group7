import csv
from transcript_parser.transcript_parser import FieldNames


class AddCountOccurrenceColumn:
    data_set: [[]] = None
    str_to_count: str = None
    filename: str = None

    def __init__(self, filename: str, str_to_count: str):
        self.str_to_count = str_to_count.lower()
        self.data_set = []
        self.filename = filename

        self.read_file()
        self.add_counts()

    def read_file(self):
        with open(self.filename, 'r', encoding="utf-8") as f:
            csv_reader = csv.reader(f)

            for row in csv_reader:
                self.data_set.append(row)

    def add_counts(self):
        size = len(self.data_set)

        # Adding a header to the first row for this count
        self.data_set[0].append(f"\"{self.str_to_count}\" count")

        for row in range(1, size):
            self.data_set[row].append(self.count_occurrence(self.data_set[row]))

    def count_occurrence(self, data_row: [str]) -> int:
        transcript = data_row[FieldNames.transcript].lower()

        return transcript.count(self.str_to_count)
