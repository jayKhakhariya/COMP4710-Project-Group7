from transcript_parser.transcript_parser import FieldNames
import csv
import constants


class ConcatDataSet:
    all_datasets = None
    all_talk_ids = None

    def __init__(self):
        self.all_talk_ids = set()
        self.all_datasets = []
        self.concat_datasets()

    def concat_datasets(self):
        for filename in constants.all_datasets:
            with open(filename, 'r', encoding="utf-8") as f:
                csv_reader = csv.reader(f)
                self.add_rows(csv_reader)

    def add_rows(self, csv_reader):
        for row in csv_reader:
            talk_id = row[FieldNames.talk_id]

            if talk_id not in self.all_talk_ids:
                self.all_talk_ids.add(talk_id)
                self.all_datasets.append(row)


print(f"There are {len(ConcatDataSet().all_datasets)} unique talks "
      f"across all languages.")
