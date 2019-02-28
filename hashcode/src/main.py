import random

def find_ver_pair(photo, ver):
    #find the best vertical photo to match with photo

    
    return 
def make_slides(hor, ver):
    slides = []

    #all horizontal photos make 1 slide
    for i in range(len(hor)):
        slides.append([ hor[i]['id'], hor[i]['tags'])

    #make slides with vertical photos
    j = 0
    while len(ver) >= 2:
        ver1 = random.randint(0,len(ver))
        ver2 = find_ver_pair(ver1, ver)
        slides.append([ ver[ver1]['id'], ver[ver2]['id'], ver[ver1]['tags'].update(ver[ver2]['tags']) ])
        del ver[ver1]
        del ver[ver2]

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
