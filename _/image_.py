import PIL.Image as Image
import os

def binarization_spec(file_path):
    image = Image.open(file_path)
    pixels = image.load()
    for x in range(image.width):
      for y in range(image.height):
        if pixels[x, y]==(249,249,249):
            pixels[x, y]=(255,255,255)
        elif pixels[x, y]==(221,221,221):
            pixels[x, y]=(255,255,255)
        else:
            pixels[x, y]=(0,0,0)
    image.save('.'.join(file_path.split('.')[:-1])+'_bin.'+file_path.split('.')[-1])
    return '.'.join(file_path.split('.')[:-1])+'_bin.'+file_path.split('.')[-1]

def covert01(pixel):
    if pixel==(0,0,0):
        return 1
    elif pixel==(255,255,255):
        return 0
    else:
        return 0

def load_image(path):
    item_ = path
    name = item_
    try:
        image = Image.open(item_)
    except:
        print 0,item_,0
    pixels = image.load()
    data = []
    data.append(image.width)
    data.append(image.height)
    image_str = ''
    for x in range(image.width):
        for y in range(image.height):
            image_str+=str(covert01(pixels[x,y]))
    data.append(image_str)
    data.append(name)
    return data

def load_dictionary(path='directionary'):
    list_ = os.listdir(path)
    loads = []
    for item in list_:
        data = []
        image_str = ''
        item = path+os.sep+item
        data = load_image(item)
        loads.append(data)
    return loads

def ximage_str(str0,str1):
    try:
        if len(str0)!=len(str1):
            return 0.0
        else:
            count = 0
            for i in range(len(str0)):
                if str0[i]==str1[i]:
                    count+=1
            return float(count)/float(len(str0))
    except:
        return 0.0

def compare_picture(image,directionary):
    for i in range(len(directionary)):
        xi = ximage_str(load_image(image)[-2],directionary[i][-2])
        directionary[i].append(xi)
    max_ = 0.0
    data = None
    for item in directionary:
        if item[-1]>max_:
            max_=item[-1]
            data=item
    return data
