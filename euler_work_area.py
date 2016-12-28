__author__ = 'tgheinze'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# f = open('/Users/tgheinze/stations.txt', 'r')
#
# for line in f:
#     if 'US' in line and 'MN' in line:
#         print(line)


msp2016 = open('/Users/tgheinze/726580-14922-2016.op', 'r')
df2016 = pd.read_csv(msp2016, sep='\s+', header=0, index_col=False)

print(df2016)


# ax = df2016[['YEARMODA','TEMP']].plot(kind='line', title ="2016 Temperatures", figsize=(15, 10), legend=True, fontsize=12)
# ax.set_xlabel("Date", fontsize=12)
# ax.set_ylabel("Temp", fontsize=12)
# plt.show()

ax = df2016[['TEMP']].plot(kind='line', title ="2016 Temperatures", figsize=(15, 10), legend=True, fontsize=12)
ax.set_xlabel("Day", fontsize=12)
ax.set_ylabel("Temp F", fontsize=12)
plt.show()



raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
#print(df)


