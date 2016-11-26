import cv2
import urllib 
import ImageLoadAndSave as ImgFuncs
import numpy as np
import AESCipherImplementation as AES128
import MD5HashFunc as MD5
import Keys 
import socket
aes = AES128.AESCipher(MD5.create_MD5Hash(Keys.e2e_key),32)
#aes_server = AES128.AESCipher(MD5.create_MD5Hash(Keys.s2s_key),32)
stream=urllib.urlopen('http://192.168.43.134:4747/mjpegfeed?320x240')
bytes=''
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('192.168.1.105',37000))
while True:
    bytes+=stream.read(512)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        encc = aes.encrypt(jpg) # If using Python 2.x use: print serial_line
	#encc_server = aes_server.encrypt("sender_id:123 "+"receiver_id:456 "+encc.decode("utf-8"))
        #decc_server = aes_server.decrypt(encc_server)
        decc = aes.decrypt(encc)
        i = cv2.imdecode(np.fromstring(decc, dtype=np.uint8),cv2.IMREAD_COLOR)
        cv2.imshow('decrypted',i)       
        #sock.send(encc_server)
        if cv2.waitKey(1) ==27:
            sock.close()
            exit(0)   


