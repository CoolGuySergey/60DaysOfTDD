# Write the smallest program that outputs the lyrics of the Xmas
# carol The Twelve Days of Xmas. You must reproduce the words in
# the correct order, but case, format, and punctuation are left
# to your discretion.

def counter_lines_writer(i): 
    
    if i < 4:
        add_on = {1: "st", 2: "nd", 3: "rd"}
        i = str(i) + add_on[i]
    else:
        i = str(i) + "th"
        
    return i


def gifts_list_writer(n):
    
    day_list = ["Twelve drummers drumming,",
                "Eleven pipers piping,",
                "Ten lords a-leaping,",
                "Nine ladies dancing,",
                "Eight maids a-milking,",
                "Seven swans a-swimming,",
                "Six geese a-laying,",
                "Five golden rings,",
                "Four calling birds,",
                "Three french hens,",
                "Two turtle doves and",
                "A partridge in a pear tree.",
                ]

    gifts_list = day_list[-n:]

    return gifts_list

def constructor():
    
    for i in range (1, 13):
        day = counter_lines_writer(i)
        gifts = gifts_list_writer(i)
        print (f"On the {day} day of Christmas\nMy true love gave to me:")
        print ("\n".join(gifts))
        print ("\n")
