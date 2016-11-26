import cv2
import urllib 
import ImageLoadAndSave as ImgFuncs
import numpy as np
from PIL import Image
import StringIO
#rom PIL import ImageFile
#ImageFile.LOAD_TRUNCATED_IMAGES = True
stream=urllib.urlopen('http://192.168.43.134:4747/mjpegfeed?320x240')
bytes=''
image_name='12345.jpg'
#fh = open(image_name,"wb")
while True:
    bytes+=stream.read(512)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        cv2.imshow('i',i)
        if cv2.waitKey(1) ==27:
            exit(0)   


