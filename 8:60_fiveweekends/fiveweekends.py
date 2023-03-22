# The month of October in 2010 has five Fridays, five Saturdays, and five Sundays.

# Task
# 1. Write a program to show all months that have
# this same characteristic of five full weekends from
# the year 1900 through 2100 (Gregorian calendar).
# 2. Show the number of months with this property
# (there should be 201).
# 3. Count and/or show all of the years which do not
# have at least one five-weekend month (there should
# be 29).

from datetime import date
from numpy import busday_count

def weekend_counter(year, month):

    start = date(year, month, 1)
    
    if month == 12:
        end = date(year+1, 1, 1)

    else:
        end = date(year, month+1, 1)

    weekend_days = (end-start).days - busday_count(start, end)

    no_of_weekends = int(weekend_days / 2)

    return no_of_weekends

def starts_on_fri(year, month):

    return date(year, month, 1).isoweekday() == 5

def five_wknds_months_lister(start_year, end_year):

    all_months = [(i, j)
                  for i in range(start_year, end_year+1)
                  for j in range(1, 13)]

    target_months = [(year, month) for year, month in all_months if weekend_counter(year, month) == 5 and starts_on_fri(year, month)]

    return target_months

def horrible_year_lister(start_year, end_year):
    
    # Find years which do not have a 5-wknd month

    good_months = five_wknds_months_lister(start_year, end_year)
    good_years = list(dict(good_months).keys())

    results = [year for year in range(start_year, end_year+1) if year not in good_years]

    return results
