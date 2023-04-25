# Write a program to check is a password is strong or weak

count=0
i=0
num=0
sm=0
a="Chmo@5627"
if(len(a)>=8):
    print("true")
    for z in a:
        if z.isupper():
            count+=1
        if z.islower():
            sm+=1
        if z.isdigit():
            i+=1
        if not z.isalnum():
            num+=1  
    if(count>0 and num>0 and i>0 and sm>0):
        print("Correct")      
    else:
        print("Incorrect")      

else:
    print("false")   

        

