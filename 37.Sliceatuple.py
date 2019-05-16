#create a tuple
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
#used tuple[start:stop] the start index is inclusive and the stop index
_slice = tuplex[3:5]
 #is exclusive
print(_slice)
 #if the start index isn't defined, is taken from the beg inning of the tuple
_slice = tuplex[:6]
print(_slice)
 #if the end index isn't defined, is taken until the end of the tuple
_slice = tuplex[5:]
print(_slice)
