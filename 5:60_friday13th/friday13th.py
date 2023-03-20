# Write a program to show that the 13th day of the month falls more often
# on a Friday than any other day of the week. The 1st of January 1973 was a
# Monday. You should aim at producing the clearest possible program, not
# the fastest.

def thirteenth_in_jan(start_day):

    return list(range(1,8))[start_day-3]

def thirteenth_rest_of_year(day_of_jan_thirteenth):

    days_in_months = [31, 28, 31, 30, 31,
                      30, 31, 31, 30, 31,
                      30, 31]

    day_of_prev_thirteenth = day_of_jan_thirteenth
    list_of_thirteenths = [day_of_jan_thirteenth]
    
    for month in days_in_months:

        off_set = month % 7
        cur_thirteenth = (day_of_prev_thirteenth + off_set) % 7
        if cur_thirteenth == 0:
            cur_thirteenth = 7
        
        list_of_thirteenths.append(cur_thirteenth)
        day_of_prev_thirteenth = cur_thirteenth

    return list_of_thirteenths

def leap_year(list_of_13ths):
    
    affected_months = [(d+1)%7 for d in list_of_13ths[2:]]

    new_list = list_of_13ths[:2] + affected_months
    adjusted_list = [7 if d==0 else d for d in new_list]

    return adjusted_list

# ============================================================

from collections import Counter

counts = Counter()
first_13th = thirteenth_in_jan(1)

for year in range(1973, 9999):

    all_13ths = thirteenth_rest_of_year(first_13th)

    if year % 4 == 0:
        all_13ths = leap_year(all_13ths)
        
    new_counts = Counter(all_13ths[:-1])
    counts += new_counts

    first_13th = all_13ths[-1]

print(counts)
