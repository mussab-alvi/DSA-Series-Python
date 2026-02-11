from array import *
val=array('i',[1,2,3,4,5,6,7])
val.pop(3)   # without index LIFO (stack) pricipal works 
val.remove(5)  # if index is not knowm then remove function is helpful
for x in val:
    print(x,end=" ")