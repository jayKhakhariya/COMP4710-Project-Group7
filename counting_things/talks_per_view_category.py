import constants
import csv
import matplotlib.pyplot as plt
from transcript_parser.transcript_parser import FieldNames


data_set = []
filename = constants.transcript_en_loc

with open(filename, 'r', encoding="utf-8") as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        data_set.append(row)

view_count_categories = [1e4, 1e5, 1e6, 1e7, 1e8]
view_category_counts = [0 for _ in view_count_categories]

# skip the first (title) row of the dataset
for talk in data_set[1:]:
    view_count = int(talk[FieldNames.views])

    for i in range(len(view_count_categories)):
        if view_count <= view_count_categories[i]:
            view_category_counts[i] += 1
            break

for i in range(len(view_count_categories)):
    print(f"{view_count_categories[i]} : {view_category_counts[i]}")

plt.scatter(view_count_categories, view_category_counts)
plt.title("Number of Talks per View Category")
plt.ylabel("Number of Talks")
plt.xlabel("View Category")
plt.xscale('log')
plt.show()
