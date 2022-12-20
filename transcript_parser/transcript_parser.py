import csv
import re  # regex
import constants


"""
; will be considered as a comma, which we're removing.
, are removed
" are removed
. are considered as separate transactions.
? are considered as separate transactions.
! are considered as separate transactions.
"""


class Parser:
    _clean_sentences = []

    _view_count_categories = [10000.0, 100000.0, 1000000.0, 10000000.0, 100000000.0]

    def __init__(self, filename: str):
        
        transcript_list = self.read_transcripts(filename)
        self._clean_sentences = self.clean_transcripts(transcript_list)
        self._topics = self.read_topics_by_viewcount(filename)

    def read_transcripts(self, filename: str) -> [str]:
        transcripts = []

        with open(filename, 'r', encoding="utf-8") as f:
            csv_reader = csv.reader(f)

            for row in csv_reader:
                transcripts.append(row[FieldNames.transcript])

            return transcripts[1:]  # don't care about the header

    def read_topics_by_viewcount(self, filename: str) -> [[str]]:

        topics = [[] for _ in range(len(self._view_count_categories))]

        with open(filename, 'r', encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            csv_reader.__next__() # skip the first line
            for row in csv_reader:
                t = row[FieldNames.topics].replace('[', "").replace(']', "").replace("'", "").split(",")
                viewCount = row[FieldNames.views] 
                for category in range(len(self._view_count_categories)):
                    if(int(viewCount) < self._view_count_categories[category]):
                        topics[category].append(t)
                        break

            return topics

    def clean_transcripts(self, transcript_list: [str]) -> [[str]]:
        punctuations_to_remove = [';',
                                  ',',
                                  ':',
                                  '—',
                                  '\"',
                                  '\' ',
                                  ' \'']

        with open(constants.blacklist_loc, 'r') as f:
            blacklist = set(f.read().splitlines())

        sentences = []

        for transcript in transcript_list:
            temp = transcript.lower()

            # filter out the mid sentence punctuations
            for thing in punctuations_to_remove:
                temp = temp.replace(thing, ' ')

            # splits the text on end of sentence punctuation
            temp_sentence_list = re.split("\. |\? |! ", temp)
            clean_sentences = self.remove_words(temp_sentence_list, blacklist)
            sentences.append(clean_sentences)

        return sentences

    def remove_words(self, sentence_list: [str], blacklist: set) -> [str]:
        clean_sentences = []

        for item in sentence_list:
            dirty_word_list = item.split(' ')
            clean_word_list = []

            # filters out blacklist words
            for word in dirty_word_list:
                if word != '' and word not in blacklist:
                    clean_word_list.append(word)

            # don't add empty sentences
            if len(clean_word_list) > 0:
                clean_sentences.append(clean_word_list)

        return clean_sentences

    def get_clean_sentences(self) -> [[str]]:
        return self._clean_sentences

    def get_topics(self) -> [[str]]:
        return self._topics


# the header positions in the csv file
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


# opens and parses the english ted talk csv file
transcript_sentences = Parser(constants.transcript_en_loc).get_clean_sentences()
