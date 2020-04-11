import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Get dates and high temperatures from file
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs = [],[]
    for row in reader:
        dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
        highs.append(int(row[1]))


fig = plt.figure(dpi = 128,figsize = (10,6))
plt.plot(dates,highs,c='red')

# Format plot.
plt.title("Daily High Temperatures, July 2014", fontsize = 24)
plt.xlabel('',fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize = 16)
plt.tick_params(axis='both',which = 'major',labelsize=16)

plt.savefig('Graphs_and_Images/highs.png')
plt.show()
""" 
for index, column_header in enumerate(header_row):
    print(index, column_header)
"""

     