x=input("Dose tin lista px(1,34,12,4,15,66,234):\n")
x=list(x)
if len(x)>4:
    #Den leitourgei an h megisth/elaxisth timh yparxei pano apo mia fora
    for i in range(2):
        x.remove(max(x))
        x.remove(min(x))
    if len(x)>0:
        mesos_oros=sum(x)/len(x)
        y=0
        for i in range(len(x)):
            y=y+x[i]**2
        mesos_oros_tet=y/len(x)
        a = mesos_oros_tet - mesos_oros**2
        s=a**(0.5)
        print "Tupikh apoklish:",s
    else:
        print "H lista xoris tis dio megaliteres kai dio mikroteres times einai kenh"
else:
    print "H lista xoris tis dio megaliteres kai dio mikroteres times einai kenh"
