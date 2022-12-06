import matplotlib.pyplot as plt
from transcript_parser.transcript_parser import Parser
import constants


# this is just a scrap file right now to show a concept
parser = Parser(constants.transcript_en_loc)

clean_transcript_sentences = parser.get_clean_sentences()
# will also do the original sentences (minus punctuation) when that feature
# is added to the transcript_parser code.

word_counts = {}

for talk in clean_transcript_sentences:
    for sentence_list in talk:
        for word in sentence_list:

            # initialize the count
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1

print(f"There are {len(word_counts)} unique non-blacklist words. "
      "The words, with their associated counts, are:")

unique_words = sorted(word_counts.keys())
unique_word_counts = []

for word in unique_words:
    if word_counts[word] > 100:
        print(f"{word}: {word_counts[word]}")
    unique_word_counts.append(word_counts[word])

plt.bar(unique_words, unique_word_counts)
plt.show()
