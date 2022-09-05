import math as m
import random
#one player code


# <--------------------------------------------------------------------------------------->
# -------------------------===================ONE PLAYER=====================--------------

def one_player():
    print("===1 PLAYER GAME===")
    print(":::: <--- YOU --> X ::::")
    print(":::: <--- COMPUTER --> O ::::")
    print("\n")
    #Tic tac toe table size
    s=3
    #initializing all blocks to empty
    g=[[0 for i in range(s)] for j in range(s)]
    k=1
    for i in range(s):
        for j in range(s):
            g[i][j]=k
            k=k+1
    #changing positions
    pipe=[0,0]
    pipe[0]=1
    #counting filled blocks
    k=0
    #points of players
    p1=0
    p2=0
    #initailizing all empty blocks as X
    z=[['E' for i in range(s)] for j in range(s)]
    while(k!=(s*s)):
        print("\n")
        print("   ===   ===   ===   ====               ")
        print("   TIC   TAC   TOE   GAME               ")
        print("   ===   ===   ===   ====               ")
        print("\n")
        print("======================================")
        for i in range(s):
            for j in range(s):
                if(z[i][j]=='x'):
                    print('x',end=" ")
                elif(z[i][j]=='o'):
                    print('o',end=" ")
                else:
                    print(g[i][j],end=" ")
            print("\n")
        print("======================================")
        k+=1
        z1=[1,2,3,4,5,6,7,8,9]
        if(pipe[0]):
            print("Your Chance Now....")
            print("ENTER POSITION FOR X :: ")
            p=int(input())
            z1.remove(p)
        if(pipe[1]):
            print("Computer's Chance Now....")
            p=random.choice(z1)
            print(" <-----Computer Choosen position ---> ",int(p))
            z1.remove(p)
        p=int(p)
        p-=1
        if(pipe[0]):
            q="x"
        elif(pipe[1]):
            q="o"
        print("======================================")
        #if input is X
        if(q=="x"):
            a=int(p/s)
            b=int(p%s)
            c=0
            d=0
            z[a][b]='x'
            #total 12 ways
            #1st way
            if((b+2)<s):
                if(z[a][b+1]=='x' and z[a][b+2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #2nd way
            if((a+2)<s and (b+2)<s):
                if(z[a+1][b+1]=='x' and z[a+2][b+2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #3rd way
            if((a+2)<s):
                if(z[a+1][b]=='x' and z[a+2][b]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #4th way
            if((a+2)<s and (b-2)>=0):
                if(z[a+1][b-1]=='x' and z[a+2][b-2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #5th way
            if((b-2)>=0):
                if(z[a][b-1]=='x' and z[a][b-2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #6th way
            if((a-2)>=0 and (b-2)>=0):
                if(z[a-1][b-1]=='x' and z[a-2][b-2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #7th way
            if((a-2)>=0):
                if(z[a-1][b]=='x' and z[a-2][b]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #8th way
            if((a-2)>=0 and (b+2)<s):
                if(z[a-1][b+1]=='x' and z[a-2][b+2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #9th way
            if((b-1)>=0 and b+1<s):
                if(z[a][b-1]=='x' and z[a][b+1]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #10th way
            if((a-1)>=0 and a+1<s):
                if(z[a-1][b]=='x' and z[a+1][b]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #11th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b-1]=='x' and z[a+1][b+1]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #12th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b+1]=='x' and z[a+1][b-1]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            p1+=c
            p2+=d
            if(c>0):
                pipe[0]=1
            elif(d>0):
                pipe[1]=1
            elif(pipe[0]):
                pipe[1]=1
                pipe[0]=0
            elif(pipe[1]):
                pipe[1]=0
                pipe[0]=1
        elif(q=="o"):
            a=int(p/s)
            b=int(p%s)
            c=0
            d=0
            z[a][b]='o'
            #total 12 ways
            #1st way
            if((b+2)<s):
                if(z[a][b+1]=='o' and z[a][b+2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #2nd way
            if((a+2)<s and (b+2)<s):
                if(z[a+1][b+1]=='o' and z[a+2][b+2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #3rd way
            if((a+2)<s):
                if(z[a+1][b]=='o' and z[a+2][b]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #4th way
            if((a+2)<s and (b-2)>=0):
                if(z[a+1][b-1]=='o' and z[a+2][b-2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #5th way
            if((b-2)>=0):
                if(z[a][b-1]=='o' and z[a][b-2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #6th way
            if((a-2)>=0 and (b-2)>=0):
                if(z[a-1][b-1]=='o' and z[a-2][b-2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #7th way
            if((a-2)>=0):
                if(z[a-1][b]=='o' and z[a-2][b]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #8th way
            if((a-2)>=0 and (b+2)<s):
                if(z[a-1][b+1]=='o' and z[a-2][b+2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #9th way
            if((b-1)>=0 and b+1<s):
                if(z[a][b-1]=='o' and z[a][b+1]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #10th way
            if((a-1)>=0 and a+1<s):
                if(z[a-1][b]=='o' and z[a+1][b]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #11th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b-1]=='o' and z[a+1][b+1]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            #12th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b+1]=='o' and z[a+1][b-1]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===You got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Computer got a Point===")
                        break
            p1+=c
            p2+=d
            if(c>0):
                pipe[0]=1
            elif(d>0):
                pipe[1]=1
            elif(pipe[0]):
                pipe[1]=1
                pipe[0]=0
            elif(pipe[1]):
                pipe[1]=0
                pipe[0]=1
        else:
            k-=1
        print("==========================================")
        print("\n")
    print("======================================")
    for i in range(s):
        for j in range(s):
            if(z[i][j]=='x'):
                print('x',end=" ")
            elif(z[i][j]=='o'):
                print('o',end=" ")
            else:
                print(g[i][j],end=" ")
        print("\n")
    print("======================================")
    print("==============================================")
    print("\n")
    print("\n")
    print("GAME OVER")
    print("\n")
    print("\n")
    print("===============================================")
    if(c>d):
        print(":::::: You WINS ::::::")
    elif(c<d):
        print("::::: Computer wins ::::::")
    else:
        print(".......======DRAW=======........")


# <--------------------------------------------------------------------------------------->
# -------------------------===================TWO PLAYER=====================--------------


#two player code
def two_players():
    print("===2 PLAYER GAME===")
    print("PLAYER 1 IS x ::::")
    print("PLAYER 2 IS o ::::")
    print("\n")
    #Tic tac toe table size
    s=3
    #initializing all blocks to empty
    g=[[0 for i in range(s)] for j in range(s)]
    k=1
    for i in range(s):
        for j in range(s):
            g[i][j]=k
            k=k+1
    #changing positions
    pipe=[0,0]
    pipe[0]=1
    #counting filled blocks
    k=0
    #points of players
    p1=0
    p2=0
    #initailizing all empty blocks as X
    z=[['E' for i in range(s)] for j in range(s)]
    while(k!=(s*s)):
        print("\n")
        print("   ===   ===   ===   ====               ")
        print("   TIC   TAC   TOE   GAME               ")
        print("   ===   ===   ===   ====               ")
        print("\n")
        print("======================================")
        for i in range(s):
            for j in range(s):
                if(z[i][j]=='x'):
                    print('x',end=" ")
                elif(z[i][j]=='o'):
                    print('o',end=" ")
                else:
                    print(g[i][j],end=" ")
            print("\n")
        print("======================================")
        k+=1
        if(pipe[0]):
            print("Player 1's Chance Now....")
            print("ENTER POSITION FOR X :: ")
        if(pipe[1]):
            print("Player 2's Chance Now....")
            print("ENTER POSITION FOR O :: ")
        p=int(input())
        p-=1
        if(pipe[0]):
            q="x"
        elif(pipe[1]):
            q="o"
        print("======================================")
        #if input is X
        if(q=="x"):
            a=int(p/s)
            b=int(p%s)
            c=0
            d=0
            z[a][b]='x'
            #total 12 ways
            #1st way
            if((b+2)<s):
                if(z[a][b+1]=='x' and z[a][b+2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #2nd way
            if((a+2)<s and (b+2)<s):
                if(z[a+1][b+1]=='x' and z[a+2][b+2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #3rd way
            if((a+2)<s):
                if(z[a+1][b]=='x' and z[a+2][b]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #4th way
            if((a+2)<s and (b-2)>=0):
                if(z[a+1][b-1]=='x' and z[a+2][b-2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #5th way
            if((b-2)>=0):
                if(z[a][b-1]=='x' and z[a][b-2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #6th way
            if((a-2)>=0 and (b-2)>=0):
                if(z[a-1][b-1]=='x' and z[a-2][b-2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #7th way
            if((a-2)>=0):
                if(z[a-1][b]=='x' and z[a-2][b]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #8th way
            if((a-2)>=0 and (b+2)<s):
                if(z[a-1][b+1]=='x' and z[a-2][b+2]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #9th way
            if((b-1)>=0 and b+1<s):
                if(z[a][b-1]=='x' and z[a][b+1]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #10th way
            if((a-1)>=0 and a+1<s):
                if(z[a-1][b]=='x' and z[a+1][b]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #11th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b-1]=='x' and z[a+1][b+1]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #12th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b+1]=='x' and z[a+1][b-1]=='x'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            p1+=c
            p2+=d
            if(c>0):
                pipe[0]=1
            elif(d>0):
                pipe[1]=1
            elif(pipe[0]):
                pipe[1]=1
                pipe[0]=0
            elif(pipe[1]):
                pipe[1]=0
                pipe[0]=1
        elif(q=="o"):
            a=int(p/s)
            b=int(p%s)
            c=0
            d=0
            z[a][b]='o'
            #total 12 ways
            #1st way
            if((b+2)<s):
                if(z[a][b+1]=='o' and z[a][b+2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #2nd way
            if((a+2)<s and (b+2)<s):
                if(z[a+1][b+1]=='o' and z[a+2][b+2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #3rd way
            if((a+2)<s):
                if(z[a+1][b]=='o' and z[a+2][b]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #4th way
            if((a+2)<s and (b-2)>=0):
                if(z[a+1][b-1]=='o' and z[a+2][b-2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #5th way
            if((b-2)>=0):
                if(z[a][b-1]=='o' and z[a][b-2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #6th way
            if((a-2)>=0 and (b-2)>=0):
                if(z[a-1][b-1]=='o' and z[a-2][b-2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #7th way
            if((a-2)>=0):
                if(z[a-1][b]=='o' and z[a-2][b]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #8th way
            if((a-2)>=0 and (b+2)<s):
                if(z[a-1][b+1]=='o' and z[a-2][b+2]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #9th way
            if((b-1)>=0 and b+1<s):
                if(z[a][b-1]=='o' and z[a][b+1]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #10th way
            if((a-1)>=0 and a+1<s):
                if(z[a-1][b]=='o' and z[a+1][b]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #11th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b-1]=='o' and z[a+1][b+1]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            #12th way
            if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
                if(z[a-1][b+1]=='o' and z[a+1][b-1]=='o'):
                    if(pipe[0]):
                        c+=1
                        print("===Player 1 got a Point===")
                        break
                    if(pipe[1]):
                        d+=1
                        print("===Player 2 got a Point===")
                        break
            p1+=c
            p2+=d
            if(c>0):
                pipe[0]=1
            elif(d>0):
                pipe[1]=1
            elif(pipe[0]):
                pipe[1]=1
                pipe[0]=0
            elif(pipe[1]):
                pipe[1]=0
                pipe[0]=1
        else:
            k-=1
        print("==========================================")
        print("\n")
    print("======================================")
    for i in range(s):
        for j in range(s):
            if(z[i][j]=='x'):
                print('x',end=" ")
            elif(z[i][j]=='o'):
                print('o',end=" ")
            else:
                print(g[i][j],end=" ")
        print("\n")
    print("======================================")
    print("==============================================")
    print("\n")
    print("\n")
    print("GAME OVER")
    print("\n")
    print("\n")
    print("===============================================")
    if(c>d):
        print(":::::: Player 1 WINS ::::::")
    elif(c<d):
        print("::::: Player 2 wins ::::::")
    else:
        print(".......======DRAW=======........")
#greetings
print("===================")
print("WELCOME TO TICTACTOE GAME")
print("\n")
print("======YOO==========")
print("\n")
print("::: PLEASE CHOOSE A OPTION :::")
print("1-> PLAY WITH COMPUTER == ")
print("2-> PLAY WITH FRIEND == ")
print("3-> EXIT ==")
k9=int(input())
if(k9==1):
    one_player()
elif(k9==2):
    two_players()
else:
    exit()
#end of the code
#thanks....................
