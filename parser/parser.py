import csv
import re  # regex


"""
; will be considered as a comma, which we're removing.
, are removed
. are considered as separate transactions.
? are considered as separate transactions.
! are considered as separate transactions.
"""


class Parser:
    transcripts = []
    sentences = []

    def __init__(self, filename):
        self.get_transcripts(filename)
        self.clean_transcripts()

        test = self.sentences[0]
        for sentence in test:
            print(sentence)

    def get_transcripts(self, filename):
        with open(filename, 'r') as f:
            csv_reader = csv.reader(f)

            for row in csv_reader:
                self.transcripts.append(row[FieldNames.transcript])

            self.transcripts = self.transcripts[1:]  # don't care about the header

    def clean_transcripts(self):
        punctuations_to_remove = [';',
                                  ',',
                                  ':',
                                  '—',
                                  '\"',
                                  '\' ',
                                  ' \'']

        with open("blacklist", 'r') as f:
            blacklist = f.read().splitlines()

        for transcript in self.transcripts:
            temp = transcript.lower()

            # filter out the punctuations
            for thing in punctuations_to_remove:
                temp = temp.replace(thing, ' ')

            # filters out blacklist words
            for thing in blacklist:
                temp = re.sub(f" {thing}$|^{thing} | {thing} ", " ", temp)

            # changes all multiple spaces to a single space
            temp = re.sub(" +", ' ', temp)

            sentence_list = re.split("\. |\? |! ", temp)
            self.sentences.append(sentence_list)


class FieldNames:
    talk_id = 0
    title = 1
    speaker_1 = 2
    all_speakers = 3
    occupations = 4
    about_speakers = 5
    views = 6
    recorded_date = 7
    published_date = 8
    event = 9
    native_lang = 10
    available_lang = 11
    comments = 12
    duration = 13
    topics = 14
    related_talks = 15
    url = 16
    description = 17
    transcript = 18


Parser("../2020-05-01/ted_talks_en.csv")
