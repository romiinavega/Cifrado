import hmac
import hashlib
import binascii

#Parametros para el objeto hmac
#hmac.new(key, msg=None, digestmod="")

#Definir parametros de la función
def signature(key, msg): 
    key = binascii.unhexlify(key)
    msg = msg.encode()
    return hmac.new(key, msg, hashlib.sha256).hexdigest().upper()
print(signature("E49756B4C8FAB4E48222A3E7F3B97CC3", "ULSANOROESTE"))