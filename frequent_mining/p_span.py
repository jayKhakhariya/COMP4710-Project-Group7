import time
from prefixspan import PrefixSpan
from transcript_parser.transcript_parser import Parser
import constants

'''
Purpose:
  The purpose of this program is to run prefix span algorithm to mine the dataset with different columns 
  such as transcript, topics to identify frequent sequences and further correlate with the view count category
'''


class PSpan:
    _ps_frequent_local_sequences = []
    _global_frequent_sequences = []
    _bad_transcripts = [75, 630, 751, 900, 1062, 1358, 1704, 2010, 2715, 3131, 3307, 3651]
    our_minsup = 5

    def __init__(self, filename):
        parser = Parser(filename)
        ''' 
            the following commented code takes about 7 mins to run and only uncomment it 
            if your intention is to run the prefix span algorithm on the parsed transcripts
        '''
        transcripts = parser.get_clean_sentences()
        self._ps_frequent_local_sequences = self.prefix_span_on_transcripts(transcripts)

        self._global_frequent_sequences = PrefixSpan(self._ps_frequent_local_sequences).frequent(self.our_minsup)

    def prefix_span_on_transcripts(self, transcripts):

        frequent_sequences = []

        for transcript in range(len(transcripts)):
            if transcript not in self._bad_transcripts:
                output = self.run_prefix_span(transcripts[transcript])
                frequent_sequences.append(output)
        return frequent_sequences
    def run_prefix_span(self, transcript):
        transcript_frequent_words = PrefixSpan(transcript).frequent(self.our_minsup)

        frequent_words = []
        for sup, topic_sequence in transcript_frequent_words:
            output = f"{topic_sequence}".replace("[", "").replace("]", "")
            frequent_words.append(output)
        return frequent_words


PSpan(constants.transcript_en_loc)
