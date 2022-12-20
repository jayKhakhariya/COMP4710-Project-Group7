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

for sup, set_val in sorted_list:
    print(f"{set_val}: {size * sup}")

print(f"\nAnalysing topic data:\n")
topics = data.get_topics()
# te2 = TransactionEncoder()
# te2_ary = te2.fit(topics).transform(topics)
# df = pd.DataFrame(te2_ary, columns=te2.columns_)
# topic_results = fpgrowth(df, min_support=0.01, use_colnames=True)
# topic_list = topic_results.values.tolist()

# sorted_topic_results = sorted(topic_list)

# for sup, set_val in sorted_topic_results:
#     print(f"{set_val}: {sup}")


print(f"\nFinished.")
