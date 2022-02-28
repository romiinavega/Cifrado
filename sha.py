#importando la librería hashlib
import hashlib

#inicializando el string a cifrar
str = "ULSANOROESTE"

#encode del string
encoded_str =str.encode()

#Creamos los objetos para cada versión de SHA
hash_obj_sha224 = hashlib.sha224(encoded_str) #SHA224
hash_obj_sha256 = hashlib.sha256(encoded_str) #SHA256
hash_obj_sha384 = hashlib.sha384(encoded_str) #SHA384
hash_obj_sha512 = hashlib.sha512(encoded_str) #SHA512

# print

print("\nSha224 HAsh: " , hash_obj_sha224.hexdigest())
print("\nSha256 HAsh: " , hash_obj_sha256.hexdigest())
print("\nSha384 HAsh: " , hash_obj_sha384.hexdigest())
print("\nSha512 HAsh: " , hash_obj_sha512.hexdigest())
print("\n")
