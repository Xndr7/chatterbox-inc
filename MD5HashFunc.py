from Crypto.Hash import MD5

def create_MD5Hash(key):
        hash_obj = MD5.new()
        hash_obj.update(key)
        return hash_obj.hexdigest()
        

