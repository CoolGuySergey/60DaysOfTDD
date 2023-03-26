# Write a program to generate all potential anagrams of an input string.

# e.g. the potential anagrams of "biro" are
# biro bior brio broi boir bori
# ibro ibor irbo irob iobr iorb
# rbio rboi ribo riob roib robi
# obir obri oibr oirb orbi orib

from itertools import permutations

def anagrams(word):
    
    letters = list(str(word))
    
    return ["".join(permutation) for permutation in  permutations(letters, len(letters))]
