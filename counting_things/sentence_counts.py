from transcript_parser.transcript_parser import Parser
import constants


# this is just a scrap file right now to show a concept
parser = Parser(constants.transcript_en_loc)

clean_transcript_sentences = parser.get_clean_sentences()
# will also do the original sentences (minus punctuation) when that feature
# is added to the transcript_parser code.

sentence_count = 0

for sentence_list in clean_transcript_sentences:
    sentence_count += len(sentence_list)

print(f"There are {sentence_count} sentences in the dataset.\n"
      f"This averages to around "
      f"{int(sentence_count / len(clean_transcript_sentences))} "
      f"sentences in each talk.")
