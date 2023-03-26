from Anagrams import *

def test_anagrams():
    
    assert anagrams("biro") == ['biro', 'bior', 'brio', 'broi',
                                'boir', 'bori', 'ibro', 'ibor',
                                'irbo', 'irob', 'iobr', 'iorb',
                                'rbio', 'rboi', 'ribo', 'riob',
                                'robi', 'roib', 'obir', 'obri',
                                'oibr', 'oirb', 'orbi', 'orib']
