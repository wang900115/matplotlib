import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.scatter(view_count,likes,c=ratio,cmap='summer',
            edgecolors='black',linewidths=1,alpha=0.75)

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')
plt.yscale('log')

plt.tight_layout()

plt.show()
