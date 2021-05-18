# use Python 3
# The Star : Andrew LeBlanc, Jordan Lewis, Brian Mulhair, Bryce Ditto, Will Coker
#            Abram Bender, Brendan Buck, Troy Chiasson
  
from ftplib import FTP

method = 

# FTP server details
IP = "138.47.102.106"
PORT = 8008
USER = "thesun"
PASSWORD = "myfirstchallenge"
FOLDER = ".secretstorage/.folder2/.howaboutonemore"
USE_PASSIVE = True # set to False if the connection times out

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

# display the folder contents

words = ""

#Funtion from Brendan's binary decoder 
def Bin2Dec(binary):

    bin1 = binary
    decimal, i, n = 0, 0, 0
    
    #converts from binary to ascii value
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2,i)
        binary = binary // 10
        i += 1

    return (decimal)

#Function from Brendan's binary decoder
def sevBit(binary):
    StrOutput = " "
    #breaks binary string into 7 bit binary numbers and converts them to decimal
    # and then to a character
    for i in range(0, len(binary), 7):
        temp = int(binary[i:i+7])
        decimal = Bin2Dec(temp)
        StrOutput = StrOutput + chr(decimal)
    return StrOutput



#7 bit
if (method == 7):
    
    #loops through all files and adds the characters to a results string
    for f in files:
        bits = f[0:10]
        result = ""
        
        #checks to make sure file is not a filler file
        if (bits [0:3] == "---"):
            for x in range (len(bits)):
                #converts characters to binary
                if (bits[x] == '-'):
                    result += '0'

                else:
                    result += '1'

            #converts binary int ascii character 
            character =chr(int(result,2))

            #adds character to result string
            words += character

# 10 bit
elif (method == 10):
    all_bits = ""
    binary = ""
   
    #takes all file permissions and adds them to a string
    for f in files:
        #print (f)
        all_bits += f[0:10]
    
    #converts all permission characters to binary values
    for x in range(len(all_bits)):
        if (all_bits[x] == '-'):
            binary += '0'

        else:
            binary += '1'
    #creates final ouput from binary values using the sevBit function
    words = sevBit(binary)
        
    
        

print(words)

        
        
