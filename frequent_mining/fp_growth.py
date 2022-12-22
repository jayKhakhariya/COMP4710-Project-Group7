import pandas as pd
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
from transcript_parser.transcript_parser import Parser
import constants

data = Parser(constants.transcript_en_loc)
test = data.get_clean_sentences()

first_transcript = test[0]

our_minsup = 3.0
percent_minsup = our_minsup/len(first_transcript)
print(f"{our_minsup} converted to a percentage for this transaction is {percent_minsup}.")

te = TransactionEncoder()
te_ary = te.fit(first_transcript).transform(first_transcript)
df = pd.DataFrame(te_ary, columns=te.columns_)
results = fpgrowth(df, min_support=percent_minsup, use_colnames=True)
output_list = results.values.tolist()

size = len(first_transcript)
sorted_list = sorted(output_list)

# for sup, set_val in sorted_list:
#     print(f"{set_val}: {size * sup}")

print(f"Analysing topic data:\n")
topics = data.get_topics()
categories = data.get_viewcount_categories()

i = 0
with open("output.txt", "w") as output_file:
    for t in topics:
    
        te = TransactionEncoder()
        te_ary = te.fit(t).transform(t)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        topic_results = fpgrowth(df, min_support=0.1, use_colnames=True)
        topic_list = topic_results.values.tolist()

        sorted_topic_results = sorted(topic_list)

        output_file.write(f"\n\nTopics with at least {categories[i]} views:")
        for sup, set_val in sorted_topic_results:
            s = f"\n{set_val}: {sup}".replace("frozenset", "").replace("(", "").replace(")", "")
            output_file.write(s)
        i += 1


print(f"Analysing topics by year:\n")
topics_by_year = data.get_topics_by_year_viewcount()

i = 0
with open("topics_by_year_output.txt", "w") as output_file:
    for year in topics_by_year:
        output_file.write(f"\nFrequent Topics in the year {i}:") # should be in year - dont have it owkring
        for t in year:
            te = TransactionEncoder()
            te_ary = te.fit(t).transform(t)
            df = pd.DataFrame(te_ary, columns=te.columns_)
            topic_results = fpgrowth(df, min_support=0.6, use_colnames=True)
            topic_list = topic_results.values.tolist()

            sorted_topic_results = sorted(topic_list)

            output_file.write(f"\n\nTopics with at least {categories[i]} views:")
            for sup, set_val in sorted_topic_results:
                s = f"\n{set_val}: {sup}".replace("frozenset", "").replace("(", "").replace(")", "")
                output_file.write(s)
            i += 1
        i = 0


print(f"\n\nFinished.")
