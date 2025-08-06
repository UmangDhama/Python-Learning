

import pandas as pd
Nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
new_dict={row.letter:row.code for ( index,row) in Nato_df.iterrows()}

name=input("Enter your name : ")
lis=[char.upper() for char in name]
print(lis)

new_list = [new_dict[char] for char in lis if char in new_dict]


print(new_list)