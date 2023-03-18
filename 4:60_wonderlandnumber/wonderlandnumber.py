# You must find a way to generate the wonderland number. It has six digits.
# If you multiply it by 2, 3, 4, 5, or 6, the resulting number has all the
# same digits in at as the original number. The only difference is the
# position that they are in.

def find_wonderland_number():
    
    # loop through all possible 6-digit numbers
    for num in range(100000, 1000000):

        digits = set(str(num))
        
        if all(set(str(num * i)) == digits for i in range(2, 7)):
            return num
