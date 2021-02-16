# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# M Tu W Th F Sa Su

# Jan 1 1900 was a Monday, so every 7 days from this point is a Monday

# date[0] = year, date[1] = month, date[2] = day of month

from calendar import monthrange

def is_leap_year(date):
    year = date[0]
    if year % 100 == 0:
        if year % 400 == 0:
            return True
    else:
        if year % 4 == 0:
            return True


def leap_day_in_date_for_this_year(date) -> int:
    month = date[1]
    if is_leap_year(date):
        if month > 2 or (month == 2 and date[2] == 29):
            return 1
    return 0


def get_days_since_year_start(date):
    # print("DEBUG: {} {} {} {}".format(date, is_leap_year(date), date[0] % 100, date[0] % 400))
    month = date[1]
    day_in_month = date[2]
    # months start day, added extra 0 so I can just do days_till_month[1] for Jan, instead of [0]
    days_till_month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    return days_till_month[month] + day_in_month + leap_day_in_date_for_this_year(date)

# non-leap centurial
assert get_days_since_year_start([1900, 1, 1]) == 1
assert get_days_since_year_start([1900, 12, 31]) == 365
# leap centurial
assert get_days_since_year_start([2000, 1, 1]) == 1
assert get_days_since_year_start([2000, 12, 31]) == 366
# non-centurial non-leap year
assert get_days_since_year_start([1901, 1, 1]) == 1
assert get_days_since_year_start([1901, 12, 31]) == 365
# non-centurial leap year
assert get_days_since_year_start([1904, 1, 1]) == 1
assert get_days_since_year_start([1904, 12, 31]) == 366


def leap_days_since_1900(date):
    years = (date[0] - 1) - 1900
    # leap at 100, but then it's every 400
    non_leap_centuries = 0
    if years > 100:
        number_of_centuries_after_2000 = (years - 100) // 100
        number_of_leap_centuries_after_2000 = (years - 100) // 400
        non_leap_centuries = number_of_centuries_after_2000 - number_of_leap_centuries_after_2000
    leaps = int(years / 4) - non_leap_centuries
    leaps += leap_day_in_date_for_this_year(date)
    return int(leaps)


assert leap_days_since_1900([1900, 1, 1]) == 0
assert leap_days_since_1900([1904, 1, 1]) == 0
assert leap_days_since_1900([1904, 3, 1]) == 1
assert leap_days_since_1900([1904, 2, 29]) == 1
assert leap_days_since_1900([1904, 2, 28]) == 0


def days_since_1900(date):
    days = 0
    years = date[0] - 1900
    # '- 1' to compensate for the actual start date being the 1st of Jan
    if years > 0:
        days += (years * 365) + leap_days_since_1900(date) + get_days_since_year_start(date) - leap_day_in_date_for_this_year(date) - 1
    else:
        days += get_days_since_year_start(date) - 1
    return days


assert days_since_1900([1900, 1, 1]) == 0
assert days_since_1900([1900, 1, 2]) == 1
assert days_since_1900([1900, 12, 31]) == 364


NAME_OF_DAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def name_of_day(date):
    return NAME_OF_DAY[days_since_1900(date) % 7]


assert NAME_OF_DAY[0] == 'Monday'
assert NAME_OF_DAY[6] == 'Sunday'
assert name_of_day([1900, 1, 1]) == 'Monday'
assert name_of_day([1900, 1, 7]) == 'Sunday'

first_sunday = [1900, 1, 7]
sunday_offset = -6

# start_date = [1901, 1, 1]
# end_date = [2000, 12, 31]
# print(leap_days_since_1900(start_date))
# print(leap_days_since_1900(end_date))
# print(days_since_1900([1900, 1, 1]))
# print(days_since_1900([1900, 1, 7]))
# print(days_since_1900([1900, 1, 8]))
# print(days_since_1900(start_date))
# print(days_since_1900(end_date))

first_of_month_sundays = 0
monthrange_sundays = 0
for year in range(1901, 2000 + 1):
    for month in range(1, 12 + 1):
        cnt = 0
        if name_of_day([year, month, 1]) == 'Sunday':
            first_of_month_sundays += 1
            # print("{} sunday found! {}".format(first_of_month_sundays, [year, month, 1]))
            cnt += 1
        # Since I keep coming up with 170 as my answer.  I'm going to compare using a library
        if monthrange(year, month)[0] == 6:
            monthrange_sundays += 1
            # print("{} monthrange sunday found! {}".format(monthrange_sundays, [year, month, 1]))
            cnt += 1
        if cnt == 1:
            print("Anomaly!!! {}".format([year, month, 1]))

print("Total number of sundays that landed on first of the month {}".format(first_of_month_sundays))
print("Total number of monthrange sundays that landed on first of the month {}".format(monthrange_sundays))

# wrong answers 172
# Sunday found! [1914, 11, 1]
# Sunday found! [1915, 5, 1]  <- this is wrong, ends up being a saturday
# wrong 170 ...

# Added Anomaly counter to detect when my algorithm and monthrange do not find identical sundays.

# print(days_since_1900([2000, 12, 31]) - days_since_1900([1901, 1, 1]))
#
# print(days_since_1900([1903, 11, 1]))
# print(name_of_day([1903, 11, 1]))

# Oh dear god... way back in the days_till_month[11] array, I was returning 303 for November, when it should have been 304.
# This was the cause of my very subtle issue with calculating 170 sundays instead of 171 sundays.  Ouch.