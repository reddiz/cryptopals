import binascii
import base64

input = b'1c0111001f010100061a024b53535009181c'
xor = b'686974207468652062756c6c277320657965'

hinp = binascii.b2a_hex(input)
hxor = binascii.b2a_hex(xor)

tes = "".join(str(x ^ y) for x,y in zip(hinp, hxor))

print (str(binascii.a2b_hex(tes), 'hex'))
