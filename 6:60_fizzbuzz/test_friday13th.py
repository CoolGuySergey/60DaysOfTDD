from friday13th import *

def test_thirteenth_in_jan():

    #1st is Mon. 13th is Sat.
    assert thirteenth_in_jan(1) == 6
    assert thirteenth_in_jan(7) == 5

def test_thirteenth_rest_of_year():

    #let's say 13th Jan was Mon
    assert thirteenth_rest_of_year(1) == [1, 4, 4, 7, 2,
                                          5, 7, 3, 6, 1,
                                          4, 6, 2]
def test_leap_year():

    assert leap_year([1, 4, 4, 7, 2, 5, 7, 3, 6, 1, 4, 6, 2]) == [1, 4, 5, 1, 3, 6, 1, 4, 7, 2, 5, 7, 3]
