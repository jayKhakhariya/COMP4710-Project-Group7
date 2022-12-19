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
duration_categories = [0, 1, 2]

# find the minimum and maximum duration to build the duration_categories off of
max_duration = -1
min_duration = 1e30

for talk in data_set[1:]:
    duration_count = int(talk[FieldNames.duration])

    if duration_count > max_duration:
        max_duration = duration_count

    if duration_count < min_duration:
        min_duration = duration_count

print(f"The smallest duration is {min_duration}.")
print(f"The largest duration is {max_duration}.")

# automatically builds out the fibonacci duration_categories
while max_duration > duration_categories[-1]:
    duration_categories.append(duration_categories[-1] + duration_categories[-2])

view_count_categories = [1e4, 1e5, 1e6, 1e7, 1e8]

duration_avc = [[] for count_cat in duration_categories]

for i in range(len(duration_categories)):
    duration_avc[i] = [0 for count_cat in view_count_categories]

# skip the first (title) row of the dataset
for talk in data_set[1:]:
    duration_count_index = -1
    view_count_index = -1

    duration_count = int(talk[FieldNames.duration])
    view_count = int(talk[FieldNames.views])

    for i in range(len(duration_categories)):
        if duration_count <= duration_categories[i]:
            duration_count_index = i
            break

    for i in range(len(view_count_categories)):
        if view_count <= view_count_categories[i]:
            view_count_index = i
            break

    if view_count_index == -1:
        print(f"The view count in this talk is outside our categories. "
              f"It has a count of {view_count}.")
    else:
        duration_avc[duration_count_index][view_count_index] += 1

print(f"The final duration avc is:")

for row in duration_avc:
    print(row)

print(f"The rows are duration count categories:\n\t{duration_categories}")
print(f"The columns are view count categories:\n\t{view_count_categories}")
