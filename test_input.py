import serial, time
import AESCipherImplementation as AES128
import MD5HashFunc as MD5
import Keys 


def main:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    aes = AES128.AESCipher(MD5.create_MD5Hash(Keys.e2e_key),32)
    aes_server = AES128.AESCipher(MD5.create_MD5Hash(Keys.s2s_key),32)

    while 1:
        serial_line = ser.readline()

        encc = aes.encrypt(serial_line.decode("utf-8")) # If using Python 2.x use: print serial_line
        print ("e2e value: "+encc)
        encc_server = aes_server.encrypt("sender_id:123 "+"receiver_id:456 "+encc.decode("utf-8"))
        print ("to server value: "+encc_server)
        decc_server = aes_server.decrypt(encc_server)
        decc = aes.decrypt(decc_server.split(' ')[2])
        print("from server value: "+decc_server)
        print("real value: "+decc)
# Do some other work on the data

        time.sleep(5) # sleep 5 minutes

    # Loop restarts once the sleep is finished

    ser.close() # Only executes once the loop exits

if __name__ == "__main__":
    main()
