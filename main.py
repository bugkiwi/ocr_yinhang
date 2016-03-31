#!/usr/bin/env python
#coding:utf-8
import sys
if sys.getdefaultencoding()=='ascii':
    reload(sys)
    sys.setdefaultencoding('utf-8')

import re
import os.path

from PIL import Image
import pytesseract

if not os.path.exists("./result"):
    os.mkdir("result")

NAME = '5870b'
img = Image.open("%s.png"%NAME)
with file(NAME+".css") as f:
    css = "".join(f.readlines())

for cls in css.split("}"):
    # .b1c6xPHb{width:9px;background-position:-18px -109px;
    cls = cls.strip()
    if len(cls)>0:
        name = re.findall(r"^\.(.*){",cls)
        if len(name)<1:
            continue
        cls_name = name[0]
        width = int(re.findall(r"width:(\d+)px",cls)[0])
        position = map(int,re.findall(r"background-position:-([\d]*)px.*-([\d]*)px",cls)[0])

        box = (position[0],position[1],position[0]+width,position[1]+16)
        region = img.crop(box)
        #region.save("./result/%s.png"%cls_name)
        print cls_name,pytesseract.image_to_string(region,config="-psm 10")
