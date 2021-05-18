#The Star Binary
#Python 3.9

result = ''#empty string for 8-bit
result1 = ''#empty string for 7-bit
a = input()#input from cmd
text = []#list for 8-bit
text1 = []#list for 7-bit
#7 bit binary
if (len(a)%7==0):
    for n in range(0,len(a),7):
        #print(a[n:n+7]) #prints 7 bit binary
        num = int(''.join(a[n:n+7]),2)#converts binary into char and adds it to a list
        if(num == 8):#8 is value for backspace in ascii
            del text[len(text)-1] #deletes (backspaces) last item in the list
        else:
            text+=chr(num)#Adds new item to list
    for i in text:#concats list into readable text
        result+=i
    print(result)


#8 bit binary
if (len(a)%8==0):
    for n in range(0,len(a),8):
        num = int(''.join(a[n:n+8]),2)#converts binary into char and adds it to a list
        if(num == 8):#8 is value for backspace in ascii
            del text1[len(text1)-1] #deletes (backspaces) last item in the list
        else:
            text1+=chr(num) #Adds new item to list
        
    for j in text1:#concats list into readable text
        result1+=j
    print(result1)
        


