import math 

Tx=91055;
Ty=91055;
betaX=math.pi
betaY=math.pi
Sx=1.0005
Sy=0.99997
betaXY=math.pi*2
Sigma=1
delta=math.pi/90
a0=1.22
b0=0.732
a1=-0.23
b1=0.32
a2=1
b2=1.01
a3=3
b3=-2.92
c1=1.563
c2=0.869

def Help():
    print("This Library was created by Marios Beikos for a subject. \nThe available functions are:\n.Help\n.Translation\n.Rotation\n.Scale\n.Similarity\n.Affine\n.Projected")
    return

#translations, dilations(Scale), rotations, shearing, and reflections. (affine)
#https://towardsdatascience.com/understanding-transformations-in-computer-vision-b001f49a9e61

#Metathesi
def Translation(List):
    Tx=91055
    Ty=91055
    NewList=[["Id","X","Y"]]
    for i in range(1,len(List)):
        x=List[i][1]+Tx
        y=List[i][2]+Ty
        NewList.append([int(i),round(x,2),round(y,2)])
    return NewList,"Translation"

#Strofi
def Rotation(List):
    betaX=math.pi
    betaY=math.pi
    NewList=[["Id","X","Y"]]
    for i in range(1,len(List)):
        x=List[i][1]*math.cos(betaX) + List[i][2]*math.sin(betaY)
        y= (-1)*List[i][1]*math.sin(betaX) + List[i][2]*math.cos(betaY)
        NewList.append([int(i),round(x,2),round(y,2)])
    return NewList,"Rotation"

#Klimaka
def Scale(List):
    Sx=1.0005
    Sy=0.99997
    NewList=[["Id","X","Y"]]
    for i in range(1,len(List)):
        x= List[i][1]*Sx
        y= List[i][2]*Sy
        NewList.append([int(i),round(x,2),round(y,2)])
    return NewList,"Scale"

#Omoiotita = Similarity?
def Similarity(List):
    Tx=91055
    Ty=91055
    betaXY=math.pi*2
    Sigma=1
    a=math.cos(betaXY)*Sigma
    b=math.sin(betaXY)*Sigma
    NewList=[["Id","X","Y"]]
    for i in range(1,len(List)):
        x= a*List[i][1] + b*List[i][2] + Tx
        y= -b*List[i][1] + a*List[i][2] + Ty
        NewList.append([int(i),round(x,2),round(y,2)])
    return NewList,"Similarity"

#afinikos
def Affine(List):
    Tx=91055
    Ty=91055
    betaXY=math.pi*2
    Sx=1.000005
    Sy=0.9999997
    delta=math.pi/90
    a1=Sx*(math.cos(betaXY) + delta*math.sin(betaXY))
    b1=Sy*math.sin(betaXY)
    a2=Sy*(-math.sin(betaXY) + delta*math.cos(betaXY))
    b2=Sy*math.cos(betaXY)
    NewList=[["Id","X","Y"]]
    for i in range(1,len(List)):
        x= a1*List[i][1] + b1*List[i][2] + Tx
        y= -a2*List[i][1] + b2*List[i][2] + Ty
        NewList.append([int(i),round(x,2),round(y,2)])
    return NewList,"Affine"

#Provolikos = Reflections?
def Projected(List):
    a0=1.22
    b0=0.732
    a1=-0.23
    b1=0.32
    a2=1
    b2=1.01
    c1=1.563
    c2=0.869
    NewList=[["Id","X","Y"]]
    for i in range(1,len(List)):
        x= (a1*List[i][1]+b1*List[i][2]+c1)/(a0*List[i][1]+b0*List[i][2]+1)
        y= (a2*List[i][1]+b2*List[i][2]+c2)/(a0*List[i][1]+b0*List[i][2]+1)
        NewList.append([int(i),round(x,2),round(y,2)])
    return NewList,"Projected"

#Euclidean Distance
def EuclideanDistance(List1,List2):
    x=5
    if len(List1)!=len(List2):
        print("Lists have difference amount of points")
        return
    else: 
        NewList=["Id","Sx","Sy"]
        for i in range(1,len(List1)):
            dis = ( (List1[i][1]-List2[i][1])**2 + (List2[i][2]-List2[i][2])**2 )**0.5
            NewList.append([int(i),round(dis)])
        return NewList,x

#AverageXY
def AverageXY(List):
    NewList=["#Id","X","Y"]
    x=0
    y=0
    for i in range(1,len(List)):
        x=x + List[i][1]
        y+= List[i][2]
    x=sum(x)/(len(x)-1)
    y=sum(x)/(len(x)-1)
    x.append([int(len(List)),round(x,2),round(y,2)])
    return NewList









