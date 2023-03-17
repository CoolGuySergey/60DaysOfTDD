from hundreddoors import perfect_square_finder, perfect_square_lister

def test_perfect_square_finder():
    assert perfect_square_finder(4) == True;
    assert perfect_square_finder(3) == False;
    
def test_perfect_square_lister():
    assert perfect_square_lister(8) == [1, 4]
    assert perfect_square_lister(9) == [1, 4, 9]
    assert perfect_square_lister(10) == [1, 4, 9]
