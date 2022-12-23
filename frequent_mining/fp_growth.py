import pandas as pd
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
from transcript_parser.transcript_parser import Parser
import constants

print("\nStarting Analysis of Ted Talks\n")
outputFolder = "results/"
MIN_TALKS = 3
minsup = 0.1

data = Parser(constants.transcript_en_loc)

print(f"Analysing topic data:")

topics = data.get_topics()
categories = data.get_viewcount_categories()

i = 0
outputName = f"{outputFolder}topics_output_ms{minsup}.txt"
with open(outputName, "w") as output_file:
    output_file.write(f"Minsup = {minsup}")
    for t in topics:
        te = TransactionEncoder()
        te_ary = te.fit(t).transform(t)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        topic_results = fpgrowth(df, min_support=minsup, use_colnames=True)
        topic_list = topic_results.values.tolist()

        sorted_topic_results = sorted(topic_list)

        output_file.write(f"\n\nTopics with at least {categories[i]} views:")
        for sup, set_val in sorted_topic_results:
            s = f"\n{set_val}: {sup}".replace("frozenset", "").replace("(", "").replace(")", "")
            output_file.write(s)
        i += 1
print("Done.\n")


print(f"Analysing topics by year:")
topics_by_year = data.get_topics_by_year_viewcount()

i = 0
outputName = f"{outputFolder}topics_by_year_output_ms{minsup}.txt"
with open(outputName, "w") as output_file:
    output_file.write(f"Minsup = {minsup}")
    for (year, topics) in topics_by_year:
        output_file.write(f"\n\nFrequent Topics in the year {year}:")
        totalTalks = 0
        for t in topics:
            totalTalks += len(t)
        output_file.write(f"\nNumber of talks in {year}: {totalTalks}")

        for t in topics:
            if int(year) == 2017 and int(categories[i]) == 100000000:
                continue

            if len(t) < MIN_TALKS:
                continue
            te = TransactionEncoder()
            te_ary = te.fit(t).transform(t)
            df = pd.DataFrame(te_ary, columns=te.columns_)
            topic_results = fpgrowth(df, min_support=minsup, use_colnames=True)
            topic_list = topic_results.values.tolist()

            sorted_topic_results = sorted(topic_list)

            output_file.write(f"\n\nTopics with at least {categories[i]} views:")
            for sup, set_val in sorted_topic_results:
                s = f"\n{set_val}: {sup}".replace("frozenset", "").replace("(", "").replace(")", "")
                output_file.write(s)
            i += 1
        i = 0
print("Done.\n")


print(f"\nEnd of Process.")
