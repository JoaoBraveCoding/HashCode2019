import random

def make_ss(photos):
    slideshow = []
    current_photo = 0

    i = random.randint(0, len(photos))

    slideshow.append(photos[i])
    del photos[i]

    #pick next photo
    while len(photos) > 0:
        rand1 = random.randint(0, len(photos))
        rand2 = random.randint(0, len(photos))

        if comparePhotos(slideshow[current_photo], photos[rand1]) > comparePhotos(slideshow[current_photo], photos[rand2]):
            slideshow.append(photos[rand1])
            del photos[rand1]
            current_photo = rand1
        else:
            slideshow.append(photos[rand2])
            del photos[rand2]
            current_photo = rand2

def comparePhotos(t1,t2): #tags for p1 and p2
    common = 0
    t1NotInT2 = 0
    t2NotInT1 = 0
    for el1 in t1:
        tempResult = auxCompare(el1, t2)
        if tempResult == 1:
            common+=1
        else:
            t1NotInT2+=1

    for el2 in t2:
        tempResult = auxCompare(el2, t1)
        if tempResult == 1:
            common+=1
        else:
            t2NotInT1+=1

def auxCompare(el, t2):
    for el2 in t2:
        if(el == el2):
            return 1
    return 0

def ss_out(slideshow):
    out = ""
    out += len(slideshow)
    for i in slideshow:
        out.append(i)