import AESCipherImplementation as AES128
import ImageLoadAndSave as ImgFuncs
import MD5HashFunc as MD5
import Keys 

def main():
    '''
    - main() initilizes both encryption processes and converts them and displays the encrypted and decrypted form of parameter.
    - key management is to be done here.
    - MD5hash of the key is used. 
    '''
    aes = AES128.AESCipher(MD5.create_MD5Hash(Keys.e2e_key),32)
    aes_server = AES128.AESCipher(MD5.create_MD5Hash(Keys.s2s_key),32)
    input_image = ImgFuncs.Load_Image("lena.jpg")
    encc = aes.encrypt(input_image) # If using Python 2.x use: print serial_line
    encc_server = aes_server.encrypt("sender_id:123 "+"receiver_id:456 "+encc)
    decc_server = aes_server.decrypt(encc_server)
    decc = aes.decrypt(decc_server.split(' ')[2])
    ImgFuncs.Save_Image("456.jpg",decc)
    ImgFuncs.Save_Image("original.jpg",input_image)
    #ImgFuncs.Save_Image("457.jpg",encc)
    print(len(encc))
    print(len(encc_server))
    print(len(decc_server))
    print("ENCRYPTED STRING: "+encc+"\n")
    print("ENCRYPTED STRING TO SERVER: "+encc_server+"\n")
    print("DECRYPTED STRING FROM SERVER: "+decc_server+"\n")
    if (input_image == decc):
        print("ok")
    else:
        print("Error")
    if(encc!=decc):
        print("Not same!")

if __name__ == "__main__":
    main()
