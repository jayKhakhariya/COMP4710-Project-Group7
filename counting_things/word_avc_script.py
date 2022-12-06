import constants
from add_count_occurrence_column import AddCountOccurrenceColumn
from transcript_parser.transcript_parser import FieldNames

word = "(laughter)"
dataset_w_word = AddCountOccurrenceColumn(constants.transcript_en_loc, word).data_set

word_count_categories = [0]
step_size = 10
max_value = 80
curr_category = 0

while curr_category < max_value:
    curr_category += step_size
    word_count_categories.append(curr_category)

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

    if word_count_index == -1:
        print(f"The laugh count in this talk is outside our categories. "
              f"It has a count of {word_count}.")
    elif view_count_index == -1:
        print(f"The view count in this talk is outside our categories. "
              f"It has a count of {view_count}.")
    else:
        word_avc[word_count_index][view_count_index] += 1

print(f"The final {word} avc is:")

for row in word_avc:
    print(row)

print(f"The rows are {word} count categories:\n\t{word_count_categories}")
print(f"The columns are view count categories:\n\t{view_count_categories}")
