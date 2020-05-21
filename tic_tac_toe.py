from random import choice

p1 = input("Enter player 1 : ")

def putArr(q,p):
	""" Placing the value at correct position """
    r = q//3
    c = q%3
    if p==p1:
        arr[r][c] = "o"
    else:
        arr[r][c] = "x"

def check(a,pos):
	""" Checking if the input is correct. If not, taking input again"""
    if a not in pos:
        print("Invalid input")
        a = int(input("p1 turn : "))
        a = check(a,pos)
    return a
	
def win(x):
	""" Conditions to win the game """
	x = "WOW!!! CHAMP YOU WON"
	w = "SORRY!!! YOU LOSE"
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == "o":
            print(x)
            return True 
        elif arr[i][0] == arr[i][1] == arr[i][2] == "x":
            print(w)
            return True
        elif arr[0][i] == arr[1][i] == arr[2][i] == "o":
            print(x)
            return True
        elif arr[0][i] == arr[1][i] == arr[2][i] == "x":
            print(w)
            return True
    else:
        if arr[0][0]==arr[1][1]==arr[2][2]=="o":
            print(x)
            return True
        elif arr[0][0]==arr[1][1]==arr[2][2]=="x":
            print(w)
            return True
        elif arr[0][2] == arr[1][1] == arr[2][0]=="o":
            print(x)
            return True
        elif arr[0][2] == arr[1][1] == arr[2][0]=="x":
            print(w)
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
    show(arr)
    while len(pos):
        print("-"*50,"\n")
        print("Available position : "+str(pos))
        x = int(input("p1 turn : "))
        x = check(x,pos)
        putArr(x, p1)
        show(arr)
        t = win(arr)
        if t:
            break 
        pos.remove(x)
        print("-"*50,"\n")
        if len(pos) != 0:
            print("Available position : "+str(pos))
            x = choice(pos)
            putArr(x," ")
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
    arr = [[" "," "," "],[" "," "," "],[" "," "," "]]
    play()
    y = input("Do you want to play again(y/n)? : ").strip().lower()
else:
    print("Thank you. Come back soon")