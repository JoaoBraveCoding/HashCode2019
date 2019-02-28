def comparePhotos(t1,t2): #tags for p1 and p2
    common = 0
    t1NotInT2 = 0
    t2NotInT1 = 0
    tempResult = 0
    for el1 in t1:
        tempResult = auxCompare(el1, t2)
        if(tempResult == 1):
            common+=1
        else:
            t1NotInT2+=1

    for el2 in t2:
        tempResult = auxCompare(el2, t1)
        if(tempResult == 1)
            common+=1
        else
            t2NotInT1+=1

def auxCompare(el, t2):
    for el2 in t2:
        if(el == el2):
            return 1
    return 0
