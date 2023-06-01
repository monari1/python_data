import  csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'sitka.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print (header_row)

    # printing the header and their positions

    #for index, column_header in enumerate(header_row):
        #print (index, column_header)

        # extracting and reading the data
        # Adding and plotting for date and high temperature
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# print(highs)

#plotting data in a temperature chart using matplotlib

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
#format plot

plt.title("Dailr high temperature, July 2018", fontsize = 24)

plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()

plt.ylabel('Temperature (F)', fontsize = 16)

plt.tick_params(axis = 'both', which = 'major', labelsize = 16)


plt.show()

