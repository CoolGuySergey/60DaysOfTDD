# Write a program that prints the numbers from 1
# to 100, but...

# numbers that are exact multiples of 3, or that
# contain 3, must print a string containing "Fizz"
#   For example 9 -> "...Fizz..."
#   For example 31 -> "...Fizz..."

# numbers that are exact multiples of 5, or that contain
# 5, must print a string containing "Buzz"
#   For example 10 -> "...Buzz..."
#   For example 52 -> "...Buzz..."
   
def fizzbuzzplus(n):

    if n % 3 == 0 or "3" in str(n):
        return "Fizz"

    if n % 5 == 0 or "5" in str(n):
        return "Buzz"

    return n

results = [fizzbuzzplus(n) for n in range (1, 101)]
