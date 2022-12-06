import constants
from add_count_occurrence_column import AddCountOccurrenceColumn
from transcript_parser.transcript_parser import FieldNames

laughter = "(laughter)"
dataset_w_laughter = AddCountOccurrenceColumn(constants.transcript_en_loc, laughter).data_set

laughter_count_categories = [0]
step_size = 10
max_value = 75
curr_category = 0

while curr_category < max_value:
    curr_category += step_size
    laughter_count_categories.append(curr_category)

view_count_categories = [1e4, 1e5, 1e6, 1e7, 1e8]

laughter_avc = [[] for laugh_cat in laughter_count_categories]

for i in range(len(laughter_count_categories)):
    laughter_avc[i] = [0 for view_cat in view_count_categories]

# skip the first (title) row of the dataset
for talk in dataset_w_laughter[1:]:
    laugh_index = -1
    view_index = -1

    laugh_count = int(talk[-1])  # the last category was the one added on
    view_count = int(talk[FieldNames.views])

    for i in range(len(laughter_count_categories)):
        if laugh_count <= laughter_count_categories[i]:
            laugh_index = i
            break

    for i in range(len(view_count_categories)):
        if view_count <= view_count_categories[i]:
            view_index = i
            break

    if laugh_index == -1:
        print(f"The laugh count in this talk is outside our categories. "
              f"It has a count of {laugh_count}.")
    elif view_index == -1:
        print(f"The view count in this talk is outside our categories. "
              f"It has a count of {view_count}.")
    else:
        laughter_avc[laugh_index][view_index] += 1

print("The final laughter avc is:")

for row in laughter_avc:
    print(row)

print(f"The rows are laughter count categories:\n\t{laughter_count_categories}")
print(f"The columns are view count categories:\n\t{view_count_categories}")
