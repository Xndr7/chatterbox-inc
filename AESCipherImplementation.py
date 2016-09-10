import base64
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Hash import MD5

class AESCipher(object):
        '''
        - AESCipher is responsible for the management and initilization of the AES encryption process.
        - It contains methods to perform encryption decryption as well as padding.
        - key management to be done
        '''
        def __init__(self, key,bs):
                '''
                -Initilization of the encryption object.
                -parameters passed are key and block size for AES.
                -key is passed in its hashed form  
                '''
                self.bs = bs
                self.key = key

        def encrypt(self, raw):
                '''
                - AESCipher.encrypt() is responsible for encrypting the string passed.
                - parameter passed is a raw string.
                - returns a base64 encoded encrypted string
                - Initilization Vector(iv) is also set at random
                '''
                raw = self._pad(raw)
                iv = Random.new().read(AES.block_size)
                cipher = AES.new(self.key, AES.MODE_CBC, iv)
                return base64.b64encode(iv + cipher.encrypt(raw))

        def decrypt(self, enc):
                '''
                - AESCipher.decrypt() is responsible for decrypting the string passed.
                - parameter passed is an encrypted string.
                - returns a raw string
                - Initilization Vector(iv) is read from end of the block
                '''
                enc = base64.b64decode(enc)
                iv = enc[:AES.block_size]
                cipher = AES.new(self.key, AES.MODE_CBC, iv)
                return self._unpad(cipher.decrypt(enc[AES.block_size:]))

        def _pad(self, s):
                '''
                - AESCipher._pad() is responsible for padding the string passed.
                - parameter passed is a raw string.
                - returns a padded string to have a length of a multiple of block size
                '''
                return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

        @staticmethod
        def _unpad(s):
                '''
                - AESCipher._unpad() is responsible for unpadding the string passed.
                - parameter passed is a padded string.
                - returns an unpadded string
                '''
                return s[:-ord(s[len(s)-1:])]


