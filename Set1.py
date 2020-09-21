import base64
from binascii import unhexlify, b2a_base64
from operator import xor
import codecs
'''
Challenge 1

Convert hex to base64
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

should produce:

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
'''
initial_value = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


# There are different ways of doing this on python3:
b64 = codecs.encode(codecs.decode(initial_value,'hex'),'base64').decode()
print(b64)
# This also works
b64 = b2a_base64(initial_value.decode("hex"))
print(b64)

'''
Challenge 2

Fixed XORs

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string: 

1c0111001f010100061a024b53535009181c

 ... after hex decoding, and when XOR'd against: 
 
 686974207468652062756c6c277320657965
 
  ... should produce:

746865206b696420646f6e277420706c6179

'''

initial_value  = "1c0111001f010100061a024b53535009181c"
initial_value_2= "686974207468652062756c6c277320657965"
# Iterate over the strings , convert each char into int  then xor , reconvert to hex, strip 0x and join everything:
xor = ''.join(hex(int(a,16)^ int(b,16))[2:] for a,b in zip(initial_value,initial_value_2))
print(xor)
# Another way of doing it less pro
xor = ''

for a,b in zip(initial_value,initial_value_2):
    hexa = format(hex(int(a,16) ^ int(b,16)))
    xor += str(hexa)
print(xor)


'''
Challenge 3
Single Byte XOR cipher

 The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score. 

'''
from string import ascii_lowercase
initial_value = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
for a in ascii_lowercase:
   xor = ''
   for b in initial_value:
      hexa = hex(int(a, 16) ^ int(b, 16))
      xor += hexa
   print(xor)
