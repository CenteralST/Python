#Auther Seyed Amir Hossein Sadat Hosseini
import numpy as np
import random as rn
import math as mth
MyHome=np.zeros(10,dtype="str")
Current=0



def vacumCleaner(board,Curr):
    global Current
    Current=Curr
    CGH=list()
    for j in range(len(board)):
        if board[j]=="G":
            CGH.append(j)
    if Current==0:
        for i in range(len(CGH)):
            print("Location Your Vacum Cleaner in : ",Current)
            Current=CGH[i]
            if MyHome[CGH[i]]=="G":
                MyHome[CGH[i]]=""
                print("Room {0} Is Cleaned Becouse Near To Loc :)".format(CGH[i]))
    elif Current>0:
        dest=9
        Findest=0
        dictDi=dict()
        for i in range(len(CGH)):
            dictDi[str(CGH[i])]=abs(Current-CGH[i])
        print(dictDi)
        print(CGH)
        getind=0
        for k,h in dictDi.items():
            print(k,"   ",h)
            if dest>=h:
                print(dest," > ",h," = ",dest>h)
                dest=h
                Findest=int(k)
        print(Current,"--------",Findest)
        if Current==Findest:
            print("hHhh")
            MyHome[Findest]=""
            print("Room {0} Is Cleaned Becouse Near To Loc :)".format(Findest))
            print(MyHome)
            dictDi=dict()
            CGH=list()
            vacumCleaner(MyHome,Current)
        else:
            if Current>Findest:
                print(Current,">>>>>",Findest)
                Curr=Current
                while Curr>=Findest:
                    Current=Curr
                    if MyHome[Curr]=="G":
                        MyHome[Curr]=""
                        print("Room {0} Is Cleaned Becouse Near To Loc :)".format(Curr))
                        print(MyHome)
                        dictDi=dict()
                        CGH=list()
                        vacumCleaner(MyHome,Current)
                    Curr-=1
            elif Current<Findest:
                print(Current,"<<<<<",Findest)
                for o in range(Current,Findest+1,1):
                    Current=o
                    if MyHome[o]=="G":
                        MyHome[o]=""
                        print(MyHome)
                        print("Room {0} Is Cleaned Becouse Near To Loc :)".format(o))
                        dictDi=dict()
                        CGH=list()
                        vacumCleaner(MyHome,Current)




                
def HomeReset():
    for i in range(0,5):
        ind=rn.randint(0,9)
        MyHome[ind]="G"
        
HomeReset()
State="y"
while State=="y":
    print(MyHome)
    vacumCleaner(MyHome,Current)
    print("Location Your Vacum Cleaner in : ",Current)
    print(MyHome)
    State=input("Are You Want Reset Home ?")
    if State=="y":
        HomeReset()
    else:
        State="n"
