import random
"""Problem #2
Two player dice game.
Each player will roll the die (numbers from 1 to 6)
Points are added to each roll.
1 - 1 pt
2 - 5 pts
3 - 15 pts
4 - (-15) pts
5 - (-5) pts
6 - (-1) pts"""

rows,cols=6,6
arr = [[0 for i in range(cols)] for j in range(rows)]

user1,user2=0,0
def dice(name):
    global user1,user2
    rownum = random.randint(1,6)
    print("row:",rownum-1)
    colnum = random.randint(1,6)
    print("col:",colnum-1)
    
    
    if arr[rownum-1][colnum-1]=="A" or arr[rownum-1][colnum-1]=="R":
        if arr[rownum-1][colnum-1]=="A":
            user1+=1
            print("point user1:",user1)
        else:
            user2+=1
            print("point user2:",user2)
    else:
        arr[rownum-1][colnum-1]=name
    for prn in arr:
        print(prn)
    if user1==5 or user2==5 :
        print(f"----{name}  WIN!!!------")
        return 1
    
while True:
    n=int(input("____________________________________\n1.user1 to roll dice\n2.user2 to roll dice\n3.exit\n"))
    if n==1:
        if dice("A"):
            break
    elif n==2:
        if dice("R"):
            break
    elif n==3:
        break
    else:
        print("Enter valid number")


    