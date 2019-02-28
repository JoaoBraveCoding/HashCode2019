import random
import sys

photos = []
photosV = []
photosH = []


def find_ver_pair(photo, ver):
    # find the best vertical photo to match with photo

    
    return 


def make_slides(hor, ver):
    slides = []

    # all horizontal photos make 1 slide
    for i in range(len(hor)):
        slides.append([[hor[i]['id']], hor[i]['tags']])

    # make slides with vertical photos
    while len(ver) >= 2:
        ver1 = random.randint(0, len(ver))
        ver2 = find_ver_pair(ver1, ver)
        slides.append([[ver[ver1]['id'], ver[ver2]['id']], ver[ver1]['tags'].update(ver[ver2]['tags'])])
        del ver[ver1]
        del ver[ver2]
    return slides


def make_ss(slides):
    slideshow = []
    current_slide = 0

    i = random.randint(0, len(slides))

    slideshow.append(slides[i][0])
    del slides[i]

    # pick next slide
    while len(slides) > 0:
        rand1 = random.randint(0, len(slides))
        rand2 = random.randint(0, len(slides))

        if compare_slides(slideshow[current_slide], slides[rand1]) > compare_slides(slideshow[current_slide], slides[rand2]):
            slideshow.append(slides[rand1][0])
            del slides[rand1]
            current_slide = rand1
        else:
            slideshow.append(slides[rand2][0])
            del slides[rand2]
            current_slide = rand2

    # TODO check if returns whats expected
    return slideshow


def compare_slides(s1, s2):  # tags for p1 and p2
    t1 = s1["tags"]
    t2 = s2["tags"]
    common = 0
    t1NotInT2 = 0
    t2NotInT1 = 0
    for el1 in t1:
        tempResult = aux_compare(el1, t2)
        if tempResult == 1:
            common += 1
        else:
            t1NotInT2 += 1

    for el2 in t2:
        tempResult = aux_compare(el2, t1)
        if tempResult == 1:
            common += 1
        else:
            t2NotInT1 += 1


def aux_compare(el, t2):
    for el2 in t2:
        if el == el2:
            return 1
    return 0


def ss_out(file_name, slideshow):
    out = ""
    out += str(len(slideshow)) + "\n"
    for i in slideshow:
        # TODO update this
        tempS = ""
        for j in i:
            tempS += str(j) + " "
        out += tempS + "\n"
    f = open(file_name, 'r')
    f.write(out)
    f.close()


def add_photo(line, id):
    photo = {}
    array = line.split(' ')
    photo['orientation'] = array[0]
    photo['tags'] = set(array[2:])
    photo['id'] = id
    if photo['orientation'] == 'V':
        photos.append(photo)
        photosV.append(photo)
    else:
        photos.append(photo)
        photosH.append(photo)


def main():
    # Parsing
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    f.readline()
    i = 0
    for line in f:
        add_photo(line, i)
        i += 1
    print('Photos')
    print(photos)
    print('Vertical photos')
    print(photosV)
    print('Horizontal photos')
    print(photosH)

    # Algorithm
    slides = make_slides(photosH, photosV)
    slideshow = make_ss(slides)
    # Output
    ss_out(file_name, slideshow)


if __name__ == "__main__":
    main()
