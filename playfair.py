#playfair cipher

key=input("Enter key: ")                                      #enter the key
key=key.replace(" ", "")                                      #the spaces are replaced, if any.
key=key.upper()                                               #the key letters are converted to uppercase for uniform key matrix formation

def matrix(x,y,initial):                                      #key matrix initialisation
    return [[initial for i in range(x)] for j in range(y)]
    
result=list()                                                 #initialising a list with the key matrix values
for c in key: 
    if c not in result:                               
        if c=='J':                                            #this line checks if the letter is a 'J' is it is then it is replaced with an 'I' or else the letter is appended
            result.append('I')
        else:
            result.append(c)
flag=0
for i in range(65,91): 
    if chr(i) not in result:
        if i==73 and chr(74) not in result:
            result.append("I")
            flag=1
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))
            
k=0
keymatrix=matrix(5,5,0)                                       #the values of the result list is added to the keymatrix
for i in range(0,5): 
    for j in range(0,5):  
        keymatrix[i][j]=result[k]
        k+=1

def location(x): 
    loc=list()
    if x=='J':
        x='I'
    for i ,j in enumerate(keymatrix):
        for k,l in enumerate(j):
            if x==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt():                                                 #function for encryption
    print(keymatrix)
    msg=str(input("Enter Plain-text:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("Cipher-Text:",end=' ')
    while i<len(msg):
        loc=list()
        loc=location(msg[i])
        loc1=list()
        loc1=location(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(keymatrix[(loc[0]+1)%5][loc[1]],keymatrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(keymatrix[loc[0]][(loc[1]+1)%5],keymatrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(keymatrix[loc[0]][loc1[1]],keymatrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
                 
encrypt()
