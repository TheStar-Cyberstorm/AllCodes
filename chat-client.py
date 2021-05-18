# use Python 3
import socket
from sys import stdout
from time import time

# enables debugging output, outputs time delta of each recieved data and
# concatenated bytes
DEBUG = False

# set the server's IP address and port
ip = "138.47.102.120"
port = 31337

# covert message settings
covert_delta = 0.090
ge_delta = "1"
le_delta = "0"

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))


# receive data until EOF
covert_bin = ""
data = s.recv(1024).decode()
while (data.rstrip("\n") != "EOF"):
    if DEBUG:
        print(len(data),"'" + data + "'", end=' ')
    else:
        print(data,end="")
    #print(len(data),"'" + data + "'", end=' ')
    #stdout.write(data)


    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(1024).decode()
    t1 = time()

    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    if (DEBUG):
        print(" " + str(delta))
        #stdout.flush()

    if (delta >= covert_delta):
        covert_bin += ge_delta
    else:
        covert_bin += le_delta
    stdout.flush()

# convert covert binary to string
message = ""
i = 0
while (i <= len(covert_bin)):
    b = covert_bin[i:i+8]
    if (DEBUG):
        print(b + " " + chr(int(b, 2)))
    try:
        if (len(b) != 8):
            pass
        message += chr(int(b, 2))
    except TypeError:
        message += "?"
    i += 8
message = message[:-4]

# close the connection to the server
s.close()

# print covert message
print(message)
stdout.flush()
