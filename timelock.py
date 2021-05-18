from hashlib import md5
from datetime import datetime, timezone
import pytz

DEBUG = True
CHALLENGE = True
central = pytz.timezone("US/Central")
#epoch = input("What is the epoch time (in YYYY MM DD HH mm SS)? ")
epoch = "2020 05 07 10 00 00"
#get the timestamp of the epoch time
epochTS = datetime.strptime(epoch, '%Y %m %d %H %M %S')
epochTS = central.localize(epochTS)

#get the timestamp for the current time
#current = datetime.now(pytz.utc)
current = datetime.strptime("2015 05 07 11 47 30",'%Y %m %d %H %M %S')
current = central.localize(current)

#convert the elapsed time into an md5 hash string
elapsed = int((current - epochTS).total_seconds())
interval = elapsed%60
elapsed = str(elapsed-interval)
hash_obj = str(md5(elapsed.encode()).hexdigest())
hash_obj = str(md5(hash_obj.encode()).hexdigest())

if(DEBUG):
    print("DEBUG INFORMATION: ")
    print("\tEpoch Timestamp: ",epochTS)
    print("\tCurrent Timestamp: ",current)
    print("\tHash after MD5(MD5(Elapsed Time)): ",hash_obj)

#get the output letters from the hash string
if(CHALLENGE):
    temp_str = ''
    temp_str2 = ''
    mid_char = len(hash_obj)//2
    temp_str+=hash_obj[mid_char]
    temp_str2+=hash_obj[mid_char-1]
    print("Right Middle Char is: " + temp_str)
    print("Left Middle Char is: " + temp_str2)
    
output = ""
count = 0
i = 0
while(count<2 and i<len(hash_obj)):
    if(hash_obj[i].isalpha()):
        output+=hash_obj[i]
        count+=1
    i+=1
#get the output numbers from the hash string 
count = 0
i = len(hash_obj)-1
while(count<2 and i<len(hash_obj)):
    if(not hash_obj[i].isalpha()):
        output+=hash_obj[i]
        count+=1
    i-=1

print(output)


