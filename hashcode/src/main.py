import random

def make_ss(slides):
     slideshow = []
     current_slide = 0

     i = random.randint(0, len(slides))

     slideshow.append(slides[i])
     del slides[i]

     #pick next slide
     while (len(slides) > 0):
         rand1 = random.randint(0, len(slides))
         rand2 = random.randint(0, len(slides))

         if(compareSlides(slideshow[current_slide], slides[rand1]) > compareSlides(slideshow[current_slide], slides[rand2])):
             slideshow.append(slides[rand1])
             del slides[rand1]
             current_slide = rand1
         else:
             slideshow.append(slides[rand2])
             del slides[rand2]
             current_slide = rand2

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
