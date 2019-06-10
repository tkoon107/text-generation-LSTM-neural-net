import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir("~Documents\project_data/")
file_path = "~/Documents/project_data/creditcard.csv"

raw_data = pd.read_csv(file_path)

#Peek at data
raw_data.shape
raw_data.head()

#Check for null values
raw_data.isnull().sum().sum()

#Look at transaction amount distribution
raw_data['Amount'].describe()
raw_data['Class'].sum() #Number of fraudulent transactions
raw_data['Class'].sum() / raw_data.shape[0] * 100 #Only 0.17% of transactions are fraud
amt_dist_plot = sns.distplot(raw_data['Amount'])
amt_viol_plot = sns.violinplot(raw_data['Amount'])

#plot time vs amount
amounts = raw_data['Amount'].values
time = raw_data['Time'].values
time_series = sns.scatterplot(time, amounts)
plt.show(time_series)

plt.show(amt_dist_plot)
plt.show(amt_viol_plot)

len(raw_data[raw_data['Amount'] > 1000])