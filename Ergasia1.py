a=input("Dose tin parastasi\n")
a=list(a)
count1=0
count2=0
k=1
for i in range(len(a)):
    if count2>count1:
        k=0
    if a[i]=="(":
        count1=count1+1
    elif a[i]==")":
        count2=count2+1

if count1==count2 and k!=0:
    print ("true")
else:
    print ("false")
