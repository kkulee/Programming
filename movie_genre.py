import pandas as pd
import sys
import collections

 

hist = dict()

all_list = []

 

with open(sys.argv[1], "r") as f:

    for line in f:

        str_arr = line.strip().split("::")

        str_genre = str_arr[2].split("|")

        all_list.append(str_genre)

all_list2 = sum(all_list, [])

counts = collections.Counter(all_list2)

hist_df = pd.DataFrame(counts.items())

        

hist_df.to_csv(sys.argv[2], sep = ' ', index = False, header = False)

 
 
