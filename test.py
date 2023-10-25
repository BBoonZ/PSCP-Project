import calendar
import datetime

current_datetime = datetime.datetime.today()
year = current_datetime.year
month = current_datetime.month
day = current_datetime.day
hour = current_datetime.hour
minute = current_datetime.minute
second = current_datetime.second
microsecond = current_datetime.microsecond

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Hour: {hour}")
print(f"Minute: {minute}")
print(f"Second: {second}")
print(f"Microsecond: {microsecond}")

month_name = current_datetime.strftime('%B')
day_name = current_datetime.strftime('%A')

# Print the name of the month and the name of the day
print(f"Month: {month_name}")
print(f"Day: {day_name}")