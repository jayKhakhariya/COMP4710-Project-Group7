import pandas as pd
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
from transcript_parser.transcript_parser import Parser
import constants

test = Parser(constants.transcript_en_loc).get_clean_sentences()
first_transcript = test[0]

our_minsup = 3.0
percent_minsup = our_minsup/len(first_transcript)
print(f"{our_minsup} converted to a percentage for this transaction is {percent_minsup}.")

te = TransactionEncoder()
te_ary = te.fit(first_transcript).transform(first_transcript)
df = pd.DataFrame(te_ary, columns=te.columns_)
results = fpgrowth(df, min_support=percent_minsup, use_colnames=True)
output_list = results.values.tolist()
print(output_list)
print(type(output_list))

size = len(first_transcript)
sorted_list = sorted(output_list)

for sup, set_val in sorted_list:
    print(f"{set_val}: {size * sup}")
