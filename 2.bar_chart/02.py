import matplotlib.pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd
plt.style.use("fivethirtyeight")
language_counter = Counter()
data = pd.read_csv('data.csv')
for i in data['LanguagesWorkedWith']:
    language_counter.update(i.split(';'))
languages=[]
popularity=[]
for i in language_counter.most_common(15):
    languages.append(i[0])
    popularity.append(i[1])
languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)



plt.title("Most Popular language")
plt.xlabel("Number of People Who Use")
# plt.ylabel("Number of People Who Use")

plt.tight_layout()

plt.show()