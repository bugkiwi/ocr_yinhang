import image_
import csstool
import json
import requests
import os

def get_css_url(url='http://code.bankrate.com.cn/getProductData/financing_gRrgLT98?pos=detail'):
    respon = requests.get(url,headers={'Referer': 'http://www.yinhang.com/licaichanpin_gRrgLT98.html',})
    return json.loads(respon.content.replace(",'js')",'').replace("setAjaxData(",''))['cssfile']

def get_image_url(cssfile):
    url_base = 'http://b1r.cn/d2/%s.png'
    return url_base % cssfile.replace('.','/').split('/')[-2]

'''
try:
    os.mkdir('image')
except:
    pass
css_url = get_css_url()
css = requests.get(css_url).content
image_url = get_image_url(css_url)
image = requests.get(image_url).content
image_path = 'image'+os.sep+image_url.split('/')[-1]
f = open(image_path,'wb')
f.write(image)
f.close()
cssname = css_url.replace('/','.').split('.')[-2]
cssdata = csstool.css_parse_spec(css)
binarization_image_path = image_.binarization_spec(image_path)
csstool.cut_images(binarization_image_path,cssdata,cssname)
'''
def test(css_path,image_path):
    try:
        os.mkdir('image')
    except:
        pass
    css_url = 'http://127.0.0.1/'+css_path
    f_ = open(css_path,'rb')
    css = f_.read()
    f_.close()
    image_url = 'http://127.0.0.1/'+image_path
    f_ = open(image_path,'rb')
    image = f_.read()
    f_.close()
    image_path = 'image'+os.sep+image_url.split(os.sep)[-1]
    f = open(image_path,'wb')
    f.write(image)
    f.close()
    cssname = css_url.replace('/','.').split('.')[-2]
    cssdata = csstool.css_parse_spec(css)
    binarization_image_path = image_.binarization_spec(image_path)
    cuted_path = csstool.cut_images(binarization_image_path,cssdata,cssname)
    cuted_dir_path = os.sep.join(cuted_path.split('\\')[:-1])#?
    for item in os.listdir(cuted_dir_path):
        path_ = cuted_dir_path+os.sep+item
        directionary = image_.load_dictionary()
        print path_,image_.compare_picture(path_,directionary)[-2]
        del directionary


test('test'+os.sep+'584Gh.css','test'+os.sep+'584Gh.png')