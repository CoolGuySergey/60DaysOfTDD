from random import randrange, choice
from montyhall import montyhall

def test_setup():
    
    # should have the right number of doors
    assert len(montyhall().setup(3)) == 3
    assert len(montyhall().setup(100)) == 100
    
    # should have 1 goat regardless of number of doors
    assert sum(montyhall().setup(3)) == 1
    assert sum(montyhall().setup(100)) == 1

def test_choosers_knowing_host():
    
    assert len(montyhall().choosers_knowing_host([1, 0, 0])) == 2
    assert [1,0,0][montyhall().choosers_knowing_host([1, 0, 0])[1]] == 0

def test_choosers_blind_host():
    
    assert len(montyhall().choosers_blind_host([1, 0, 0])) == 2

def test_jumper_guest():

    assert montyhall().jumper_guest([1, 0, 0], 0, 1) == 2
    assert montyhall().jumper_guest([1, 0, 0], 2, 1) == 0
