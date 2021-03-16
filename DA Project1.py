import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#loading the dataset
df = pd.read_csv('weatherHistory.csv')
df.shape 
df.dtypes
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)
df['Formatted Date']
df.dtypes
df = df.set_index('Formatted Date')
df.head()
#after resampling
data_columns = ['Apparent Temperature (C)', 'Humidity']
df_monthly_mean = df[data_columns].resample('MS').mean()
df_monthly_mean.head()
#Plotting the variation in Apparent Temperature and Humidity with time
import seaborn as sns
import warnings
#print("Variation in Apparent Temperature and Humidity with Time")
warnings.filterwarnings("ignore")
plt.figure(figsize=(14,6))
plt.title("Variation in Apparent Temperature and Humidity with time")
sns.lineplot(data=df_monthly_mean)
###########################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==1]
print("JANUARY INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of JANUARY')
plt.show()
###########################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==2]
print("FEB INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of FEBRUARY')
plt.show()
###########################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==3]
print("March Info")
print(df1)
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of March')
plt.show()
###########################################################################################
#From the plot, we can say that humidity remained almost constant in these 10 years. Even the average apparent temperature is almost same (as peaks lie on the same line)
#retrieving the data of a particular month from every year, say April
df1 = df_monthly_mean[df_monthly_mean.index.month==4]
print("April Info")
print(df1)
print("\n")
df1.dtypes
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
#ax.set_xticks(['04-01-2006','04-01-2007','04-01-2008','04-01-2009','04-01-2010','04-01-2011','04-01-2012','04-01-2013','04-01-2014','04-01-2015','04-01-2016'])
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %m %Y'))
ax.legend(loc = 'center right')
ax.set_xlabel('Month of April')
plt.show()
##############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==5]
print("MAY INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of MAY')
plt.show()
###############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==6]
print("JUNE INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of JUNE')
plt.show()
##############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==7]
print("JULY INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of JULY')
plt.show()
###############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==8]
print("AUGUST INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of AUGUST')
plt.show()
###############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==9]
print("SEPTEMBER INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of SEPTEMBER')
plt.show()
###############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==10]
print("OCTOBER INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of OCTOBER')
plt.show()
###############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==11]
print("NOVEMBER INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of NOVEMBER')
plt.show()
###############################################################################################
df1 = df_monthly_mean[df_monthly_mean.index.month==12]
print("DECEMBER INFO")
print(df1)
print("\n")
fig, ax = plt.subplots(figsize=(15,5))
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Apparent Temperature (C)'], marker='o', linestyle='-',label='Apparent Temperature (C)')
ax.plot(df1.loc['2006-04-01':'2016-04-01', 'Humidity'], marker='o', linestyle='-',label='Humidity')
ax.legend(loc = 'center right')
ax.set_xlabel('Month of DECEMBER')
plt.show()
###############################################################################################

