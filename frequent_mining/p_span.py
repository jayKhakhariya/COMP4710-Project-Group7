import time
from prefixspan import PrefixSpan
from transcript_parser.transcript_parser import Parser
import constants


class PSpan:
    _ps_frequent_words = []
    _bad_transcripts = [75, 630, 751, 900, 1062, 1358, 1704, 2010, 2715, 3131, 3307, 3651]
    our_minsup = 3

    def __init__(self, filename):
        parser = Parser(filename)
        # transcripts = parser.get_clean_sentences()
        # self.prefix_span_on_transcripts(transcripts)
        topics = parser.get_topics()
        categories = parser.get_viewcount_categories()
        self.prefix_span_on_topics(topics, categories)

    def prefix_span_on_transcripts(self, transcripts):
        with open('./frequent_mining/output-transcripts.txt', 'w') as f:
            start = time.time()
            for transcript in range(len(transcripts)):
                if transcript not in self._bad_transcripts:
                    self.run_prefix_span(transcripts[transcript], transcript, f)
            end = time.time()
            print(f'It took about - {end - start}s to run the PrefixSpan on all transcripts except bad transcripts')

    def prefix_span_on_topics(self, topics, categories):
        ps_viewcount_categories = []
        for category in topics:
            topics_p_span = PrefixSpan(category).frequent(self.our_minsup)
            ps_viewcount_categories.append(topics_p_span)

        with open('./frequent_mining/output-topics.txt', 'w') as f:
            # ignore the 1st range since it has no views
            for i in range(1, len(topics)):
                f.write(f'Frequent topics sequences with at least {categories[i]} views:')
                for sup, topic_sequence in ps_viewcount_categories[i]:
                    output = f"\n{topic_sequence}: {sup}".replace("[", "{").replace("]", "}").replace("(", "").replace(")", "")
                    f.write(output)
                f.write('\n\n')
    def run_prefix_span(self, transcript, transcript_id, f):
        start_time = time.time()
        transcript_frequent_words = PrefixSpan(transcript).frequent(self.our_minsup)
        end_time = time.time()
        f.write(f'Prefix span on transcript {transcript_id} finished, and it took {end_time - start_time}\n')

        self._ps_frequent_words.append(transcript_frequent_words)

PSpan(constants.transcript_en_loc)
