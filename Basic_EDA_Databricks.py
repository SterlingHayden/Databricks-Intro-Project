# Databricks notebook source
# imoprt data
import pandas as pd
df1 = pd.read_csv("/dbfs/FileStore/shared_uploads/shayden@uark.edu/cbb.csv")

# COMMAND ----------

# init data inspection
print(df1.shape)
df1.head()

# COMMAND ----------

# descriptive statistics
df1.describe()

# COMMAND ----------

# Transformations. lets see what the median 2 and 3 point % by conference over the years
df_conf_percent = df1.groupby(['CONF', 'YEAR'])[['3P_O', '2P_O']].median()
df_conf_percent

# COMMAND ----------

# plotting median 2 and 3 point % over time by conference
import matplotlib.pyplot as plt

# change this to see differnt confferences or multiple conferences
df = df_conf_percent[df_conf_percent['CONF'] == 'SEC']

plt.figure(figsize=(12, 6))

for conf in df['CONF'].unique():
    data = df[df['CONF'] == conf]
    plt.plot(data['YEAR'], data['3P_O'], label='3P_O', color = 'green')
    plt.plot(data['YEAR'], data['2P_O'], label='2P_O', color = 'blue')


plt.xlabel('Year')
plt.ylabel('3P_O')
plt.title('Change in 3P_O Over the Years, Colored by CONF')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()

