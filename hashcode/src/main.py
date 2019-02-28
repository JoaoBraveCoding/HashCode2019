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

def compare_slides(s1,s2): #tags for p1 and p2
    t1 = get_all_tags(s1)
    t2 = get_all_tags(s2)
    common = 0
    t1NotInT2 = 0
    t2NotInT1 = 0
    for el1 in t1:
        tempResult = aux_compare(el1, t2)
        if tempResult == 1:
            common+=1
        else:
            t1NotInT2+=1

    for el2 in t2:
        tempResult = aux_compare(el2, t1)
        if tempResult == 1:
            common+=1
        else:
            t2NotInT1+=1

def aux_compare(el, t2):
    for el2 in t2:
        if(el == el2):
            return 1
    return 0

def get_all_tags(s):
    tags = ""
    for tgs in s.tags:
        tags += tgs
    return tags

def ss_out(slideshow):
    out = ""
    out += len(slideshow)
    for i in slideshow:
        out.append(i)
