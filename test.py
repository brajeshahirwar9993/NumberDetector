import datetime
dates=str(input('Enter the date(for example:23-02-2019):'))
day, month, year = dates.split('-')
day_name = datetime.date(int(year), int(month), int(day))
print(day_name+datetime.timedelta(1))
print(day_name.strftime("%A"))

