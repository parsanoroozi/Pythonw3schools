# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.


import datetime

x = datetime.datetime.now()
# The date contains year, month, day, hour, minute, second, and microsecond.
print(x)
print(x.year)
print(x.strftime("%A"))  # week day

# creating date object:

x = datetime.datetime(2020, 5, 17)
# The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).
print(x)


# the strftime() method:
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
print(x.strftime("%B"))  # for the name of the month
print(x.strftime("%A"))  # for the name of the week day