#Run with python3.
#XOR program 
#The star group
#Members: Brian Mulhair, Jordan Lewis, Abram Bender, Will Coker,
#           Troy Chiasson, Brendan Buck, Andrew Leblanc, Bryce Ditto

import os
import sys
import base64
import binascii

key = open("key2", "rb").read()
keyLength = len(key)

message = bytearray(sys.stdin.buffer.read())
messageLength = len(message)

key = bytearray(key)

result = bytearray(a ^ b for a, b in zip (message, key))

sys.stdout.buffer.write(result)








     
