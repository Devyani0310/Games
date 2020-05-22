p1 = input("Enter player 1 : ")
p2 = input("Enter player 2 : ")
print("\n"+"----*----"*8+"\n")

def putArr(q,p):
	""" Placing the value at correct position """
    r = q//3
    c = q%3
    if p==p1:
        arr[r][c] = "o"
    else:
        arr[r][c] = "x"
		
def check(a,pos,p):
	""" Checking if the input is correct. If not, taking input again"""
  if a not in pos:
        print("Invalid input".upper().center(20," "))
        a = int(input("{} turn : ".format(p)))
        a = check(a,pos,p)
    return a
	
def win(x):
	""" Conditions to win the game """
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == "o":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p1,p2))
            print("\n"+"----*----"*8+"\n")
            return True 
        elif arr[i][0] == arr[i][1] == arr[i][2] == "x":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p2,p1))
            print("\n"+"----*----"*8+"\n")
            return True
        elif arr[0][i] == arr[1][i] == arr[2][i] == "o":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p1,p2))
            print("\n"+"----*----"*8+"\n")
            return True
        elif arr[0][i] == arr[1][i] == arr[2][i] == "x":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p2,p1))
            print("\n"+"----*----"*8+"\n")
            return True
    else:
        if arr[0][0]==arr[1][1]==arr[2][2]=="o":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p1,p2))
            print("\n"+"----*----"*8+"\n")
            return True
        elif arr[0][0]==arr[1][1]==arr[2][2]=="x":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p2,p1))
            print("\n"+"----*----"*8+"\n")
            return True
        elif arr[0][2] == arr[1][1] == arr[2][0]=="o":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p1,p2))
            print("\n"+"----*----"*8+"\n")
            return True
        elif arr[0][2] == arr[1][1] == arr[2][0]=="x":
            print("\n"+"----*----"*8+"\n")
            print("{} WON \n{} LOSE".format(p2,p1))
            print("\n"+"----*----"*8+"\n")
            return True
			
def show(a):
	""" Printing the game board. """
    for i in range(3):
        print("-"*13)
        t1,t2,t3= tuple(arr[i])
        print(("| {} "*3+"|").format(t1,t2,t3))
    print("-"*13)
    return
	
def play():
	""" Actual code """
    pos = list(range(0,9))
    while len(pos):
        print("-"*50,"\n")
        print("Available position : "+str(pos))
        x = int(input("{} turn : ".format(p1)))
        x = check(x,pos,p1)
        putArr(x, p1)
        show(arr)
        t = win(arr)
        if t:
            break 
        pos.remove(x)
        print("-"*50,"\n")
        if len(pos) != 0:
            print("Available position : "+str(pos))
            x = int(input("{} turn : ".format(p2)))
            x = check(x,pos,p2)
            putArr(x, p2)
            show(arr)
            pos.remove(x)
            t = win(arr)
            if t:
                break 
        
    else:
        print("MATCH TIE")
    return
	
y = "y"
while(y=="y"):
    arr=[["0","1","2"],["3","4","5"],["6","7","8"]]
    show(arr)
    arr = [[" "," "," "],[" "," "," "],[" "," "," "]]
    play()
    y = input("Do you want to play again(y/n)? : ").strip().lower()
else:
    print("Thank you. Come back soon")
