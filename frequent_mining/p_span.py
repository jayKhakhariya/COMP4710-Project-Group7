import time

from prefixspan import PrefixSpan
from transcript_parser.transcript_parser import Parser
import constants

transcripts = Parser(constants.transcript_en_loc).get_clean_sentences()

our_minsup = 2

# holds the output of prefix-span algorithm on each transcript
ps_frequent_words = []
print("Number of transcripts to process - ", len(transcripts), transcripts[75])
transcript_id = 0

start_time = time.time()
transcript_frequent_words = PrefixSpan(transcripts[75]).frequent(our_minsup)
end_time = time.time()
print('Prefix span on transcript ', transcript_id, " finished, and it took, ", end_time - start_time)

# for transcript in transcripts:
#     start_time = time.time()
#     transcript_frequent_words = PrefixSpan(transcript).frequent(our_minsup)
#     end_time = time.time()
#     print('Prefix span on transcript ', transcript_id, " finished, and it took, ", end_time - start_time)
#     transcript_id += 1
#     ps_frequent_words.append(transcript_frequent_words)
#







