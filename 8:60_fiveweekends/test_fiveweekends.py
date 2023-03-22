from datetime import date

from fiveweekends import *

def test_weekend_counter():
    
    assert weekend_counter(2010, 10) == 5
    assert weekend_counter(2022, 12) == 4

def test_start_on_fri():
    assert starts_on_fri(2010, 10)
    assert starts_on_fri(2023, 3) == False

def test_five_wknds_months_lister():
    assert len(five_wknds_months_lister(1900, 2100)) == 201

def test_horrible_year_lister():
    assert len(horrible_year_lister(1900, 2100)) == 29
