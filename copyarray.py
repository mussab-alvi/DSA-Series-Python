from array import *
val=array('i',[1,2,3,4,5,6,7])
copyarray = array(val.typecode, (x*2 for x in val))
for i in range(0,len(val)):
    print(copyarray[i],end=" ")