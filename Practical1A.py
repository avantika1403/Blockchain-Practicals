from Crypto.PublicKey import RSA

key = RSA.generate(2048)
p_key = key.public_key().export_key("PEM")
priv_key = key.export_key("PEM")
print("7_GovindSaini \n")
print(p_key)
print(priv_key)