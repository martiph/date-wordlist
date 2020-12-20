import datetime
file = open("date-wordlist.txt", "a")
basedate = datetime.datetime.today()
numdays = 18616
date_list = [basedate - datetime.timedelta(days=x) for x in range(numdays)]

for date in date_list:
    file.write(date.strftime("%Y%m%d") + "\n")

file.close()