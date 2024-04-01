import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt


plt.rcParams['font.family'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False


import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot as plt


plt.rcParams['font.family'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False


df = pd.read_excel('Douban Top250 Movies2.xlsx')

df['评分'] = df['评分'].astype(str).str.extract('(\d+.\d+)', expand=False).astype(float)

df['评价数'] = df['评价数'].astype(str).str.replace('人评价', '').astype(int)
df = pd.read_excel('Douban Top250 Movies2.xlsx')

df['评分'] = df['评分'].astype(str).str.extract('(\d+.\d+)', expand=False).astype(float)

df['评价数'] = df['评价数'].astype(str).str.replace('人评价', '').astype(int)


top_rated = df.nlargest(10, '评分')
plt.figure(figsize=(10, 5))
sns.barplot(x='评分', y='影片中文名', data=top_rated)
plt.title('Top 10 评分最高的电影')
plt.xlabel('评分')
plt.ylabel('电影标题')
plt.show()


plt.figure(figsize=(10, 5))
sns.histplot(df['评分'], bins=20, kde=False)
plt.title('电影评分的分布情况')
plt.xlabel('评分')
plt.ylabel('电影数量')
plt.show()


plt.figure(figsize=(10, 5))
sns.scatterplot(x='评分', y='评价数', data=df)
plt.title('评分与评分数量的关系')
plt.xlabel('评分')
plt.ylabel('评分数量')
plt.show()


ratings_interval = pd.cut(df['评分'], bins=[0, 6, 7, 8, 9, 10], right=False)
ratings_counts = ratings_interval.value_counts().dropna()
plt.figure(figsize=(10, 6))
ratings_counts.plot.pie(autopct='%1.1f%%')
plt.title('按评分区间划分的电影比例')
plt.ylabel('')  # Hide y-label
plt.show()


plt.figure(figsize=(10, 5))
df['评分'].plot(kind='line')
plt.title('Top 250 电影的电影评分')
plt.xlabel('电影排名')
plt.ylabel('评分')
plt.show()