import time
from prefixspan import PrefixSpan
from transcript_parser.transcript_parser import Parser
import constants

transcripts = Parser(constants.transcript_en_loc).get_clean_sentences()

our_minsup = 2

# holds the output of prefix-span algorithm on each transcript
ps_frequent_words = []
bad_transcripts = [75, 630, 751, 900, 1062, 1358, 1704, 2010, 2715, 3131, 3307, 3651]


def run_prefix_span(transcript, transcript_id, f):
    start_time = time.time()
    transcript_frequent_words = PrefixSpan(transcript).frequent(our_minsup)
    end_time = time.time()
    f.write(f'Prefix span on transcript {transcript_id} finished, and it took {end_time - start_time}\n')

    ps_frequent_words.append(transcript_frequent_words)


with open('output.txt', 'w') as f:
    start = time.time()
    for transcript in range(len(transcripts)):
        if transcript not in bad_transcripts:
            run_prefix_span(transcripts[transcript], transcript, f)
    end = time.time()

    print(f'It took about - {end - start}s to run the PrefixSpan on all transcripts except bad transcripts')
