import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('heavy.csv', usecols= ['MONTH','BASEL_sunshine'])
print(df)
   
x1 = list(df[df['MONTH'] == '1']['BASEL_sunshine'])
x2 = list(df[df['MONTH'] == '2']['BASEL_sunshine'])
x3 = list(df[df['MONTH'] == '3']['BASEL_sunshine'])
x4 = list(df[df['MONTH'] == '4']['BASEL_sunshine'])
x5 = list(df[df['MONTH'] == '5']['BASEL_sunshine'])
x6 = list(df[df['MONTH'] == '6']['BASEL_sunshine'])
x7 = list(df[df['MONTH'] == '7']['BASEL_sunshine'])
x8 = list(df[df['MONTH'] == '8']['BASEL_sunshine'])
x9 = list(df[df['MONTH'] == '9']['BASEL_sunshine'])
x10 = list(df[df['MONTH'] == '10']['BASEL_sunshine'])
x11 = list(df[df['MONTH'] == '11']['BASEL_sunshine'])
x12 = list(df[df['MONTH'] == '12']['BASEL_sunshine'])

names = ['December','January','February','March','April','May','June','July','August','September','October','November']


plt.hist([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12], bins = int(180/15), normed=True, label=names)

# Plot formatting
plt.legend()
plt.xlabel('Delay (min)')
plt.ylabel('Normalized Flights')
plt.title('Side-by-Side Histogram with Multiple Airlines')
plt.yticks(names)

plt.show()