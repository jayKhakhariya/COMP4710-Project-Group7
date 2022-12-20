import constants
import csv
from transcript_parser.transcript_parser import FieldNames


data_set = []
filename = constants.transcript_en_loc

with open(filename, 'r', encoding="utf-8") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        data_set.append(row)

# first 3 values (ignoring the duplicate 1) from the fibonacci sequence
comment_categories = [0, 1, 2]

# find the minimum and maximum comment to build the comment_categories off of
max_comment = -1
min_comment = 1e30

for talk in data_set[1:]:
    comment_count = talk[FieldNames.comments]

    if comment_count != '':
        comment_count = int(comment_count)
    else:
        comment_count = 0

    if comment_count > max_comment:
        max_comment = comment_count

    if comment_count < min_comment:
        min_comment = comment_count

print(f"The smallest comment is {min_comment}.")
print(f"The largest comment is {max_comment}.")

# automatically builds out the fibonacci comment_categories
while max_comment > comment_categories[-1]:
    comment_categories.append(comment_categories[-1] + comment_categories[-2])

view_count_categories = [1e4, 1e5, 1e6, 1e7, 1e8]

comment_avc = [[] for count_cat in comment_categories]

for i in range(len(comment_categories)):
    comment_avc[i] = [0 for count_cat in view_count_categories]

# skip the first (title) row of the dataset
for talk in data_set[1:]:
    comment_count_index = -1
    view_count_index = -1

    comment_count = talk[FieldNames.comments]

    if comment_count != '':
        comment_count = int(comment_count)
    else:
        comment_count = 0

    view_count = int(talk[FieldNames.views])

    for i in range(len(comment_categories)):
        if comment_count <= comment_categories[i]:
            comment_count_index = i
            break

    for i in range(len(view_count_categories)):
        if view_count <= view_count_categories[i]:
            view_count_index = i
            break

    if view_count_index == -1:
        print(f"The view count in this talk is outside our categories. "
              f"It has a count of {view_count}.")
    else:
        comment_avc[comment_count_index][view_count_index] += 1

print(f"The final comment avc is:")

for row in comment_avc:
    print(row)

print(f"The rows are comment count categories:\n\t{comment_categories}")
print(f"The columns are view count categories:\n\t{view_count_categories}")
