import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#wth_data = pd.read_csv('CA_weather_data_janfeb17.csv', parse_dates=['DATE'], index_col=['DATE'])
wth_data = pd.read_csv('MA_Feb15.csv', parse_dates=['DATE'])
#inspect data
#print(wth_data.head())
#print(wth_data.tail())
#print(wth_data.index)
print(wth_data.columns)
#delete unneeded column
del wth_data['STATION']
#print(wth_data.head())
#index data and sort data based on town
wth_data = wth_data.set_index(['NAME', 'DATE'])
sorted_data = wth_data.sort_index()

loc=0
for index, row in sorted_data.iterrows():
    #print(sorted_data[loc:loc+50])
    if loc <= 3500:
        loc = loc + 50
    else: break
#print(sorted_data.head())
#create precip df and fill NaN for prcp and snow data with 0
sorted_precip = sorted_data[['PRCP', 'SNOW']].fillna(0)
#print(sorted_precip.head(50))
#create temp df
sorted_temp = sorted_data[['TMAX', 'TMIN']]
#print(sorted_temp.tail(50))
#Histogram of precipitation
precip= sorted_precip['PRCP']
plt.xlabel('Inches of Precipiation')
plt.ylabel('Number of days')
plt.title('MA Precipiation Feb 2015')
precip.plot(y='PRCP', kind='hist', bins=10)
plt.savefig('precip_hist.pdf')
#plt.show()
#Histogram of Snowfall
snow= sorted_precip['SNOW']
plt.xlabel('Inches of Snow')
plt.ylabel('Number of days')
plt.title('MA Snowfall totals Feb 2015')
snow.plot(y='SNOW', kind='hist', bins=10)
plt.savefig('snow_hist.pdf')
#plt.show()
#Histogram of Maximum Temperatures
tmax = sorted_temp['TMAX']
tmax.plot(y='TMAX', kind='hist', bins=20)
#sns.swarmplot(y=tmax, data=tmax)not useful in this case
plt.xlabel('Degrees F')
plt.ylabel('Number of days')
plt.title('MA Maximum Temperatures Feb 2015')
plt.savefig('tmax_hist.pdf')
#plt.show()
#Histogram of Minimum Temperatures
tmin = sorted_data['TMIN']
plt.xlabel('Degrees F')
plt.ylabel('Number of days')
plt.title('MA Minimum Temperatures Feb 2015')
tmin.plot(y='TMIN', kind='hist', bins=20)
plt.savefig('tmin_hist.pdf')
#plt.show()

#Slice based on town(name)
towns_index= ['BOSTON, MA US', 'BLUE HILL, MA US', 'ASHBURNHAM, MA US', 'AMHERST, MA US']
towns =sorted_data.loc[(towns_index, slice(None)), :]
#print(towns)
#print(towns.info())

sorted_data_noindex = sorted_data.reset_index()
print(sorted_data_noindex.info())


lst =[]
for x in sorted_data_noindex:
    count= sorted_data_noindex['NAME'].value_counts()
print(count[0:139] > 27)
        #lst= lst.append(count)
    #print(count)
#    lst.append(count)
    #if count[: , ] > 27 :
    #    print(count)
#    df.append(count['NAME'] )
#
print(count)
#print(count.values > 27)
#print(lst)
#print(lst.info())
#print(df)
