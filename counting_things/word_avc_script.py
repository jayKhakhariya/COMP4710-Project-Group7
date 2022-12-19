import constants
from add_count_occurrence_column import AddCountOccurrenceColumn
from transcript_parser.transcript_parser import FieldNames

word = "(applause)"
dataset_w_word = AddCountOccurrenceColumn(constants.transcript_en_loc, word).data_set

# first 3 values (ignoring the duplicate 1) from the fibonacci sequence
word_count_categories = [0, 1, 2]

# find the maximum word_count to build the word_count_categories off of
max_word_count = -1

for talk in dataset_w_word[1:]:
    word_count = int(talk[-1])  # the last category was the one added on

    if word_count > max_word_count:
        max_word_count = word_count

print(f"The largest count for {word} is {max_word_count}.")

# automatically builds out the fibonacci word_count_categories
while max_word_count > word_count_categories[-1]:
    word_count_categories.append(word_count_categories[-1] + word_count_categories[-2])

view_count_categories = [1e4, 1e5, 1e6, 1e7, 1e8]

word_avc = [[] for count_cat in word_count_categories]

for i in range(len(word_count_categories)):
    word_avc[i] = [0 for count_cat in view_count_categories]

# skip the first (title) row of the dataset
for talk in dataset_w_word[1:]:
    word_count_index = -1
    view_count_index = -1

    word_count = int(talk[-1])  # the last category was the one added on
    view_count = int(talk[FieldNames.views])

    for i in range(len(word_count_categories)):
        if word_count <= word_count_categories[i]:
            word_count_index = i
            break

    for i in range(len(view_count_categories)):
        if view_count <= view_count_categories[i]:
            view_count_index = i
            break

    if view_count_index == -1:
        print(f"The view count in this talk is outside our categories. "
              f"It has a count of {view_count}.")
    else:
        word_avc[word_count_index][view_count_index] += 1

print(f"The final {word} avc is:")

for row in word_avc:
    print(row)

print(f"The rows are {word} count categories:\n\t{word_count_categories}")
print(f"The columns are view count categories:\n\t{view_count_categories}")
