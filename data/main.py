from DataUtil import *

if __name__ == '__main__':
    image_paths = getAllImageData()
    print(len(image_paths['naip_2013']))
    print(len(image_paths['naip_2017']))
    print(len(image_paths['nlcd_2013']))
    print(len(image_paths['nlcd_2016']))
    print(len(image_paths['landsat_2013']))
    print(len(image_paths['landsat_2014']))
    print(len(image_paths['landsat_2015']))
    print(len(image_paths['landsat_2016']))
    print(len(image_paths['landsat_2017']))

