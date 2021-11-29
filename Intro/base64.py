hex_value = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
  
print(bytes.fromhex(hex_value))

import pybase64

# OK bytes_value = str(bytes.fromhex(hex_value))
#bytes_value = pybase64.b64encode(hex_value)

#Esta linea esta OK. Convierte la cadena de bytes en base64.
base64_message = b'r\xbc\xa9\xb6\x8f\xc1j\xc7\xbe\xeb\x8f\x84\x9d\xca\x1d\x8ax>\x8a\xcf\x96y\xbf\x92i\xf7\xbf'

print(pybase64.b64encode(base64_message))

#print(bytes_value)
