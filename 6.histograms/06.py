import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')

ages = data['Age']

bins = [10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins=bins,edgecolor='black',log=True)


median_age = 29
plt.axvline(median_age,color='#fc4f30',label='median_age')

plt.legend()

plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.show()