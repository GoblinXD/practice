import math
while True:
    N2 = int(input("Enter a number between the digits of 2 and 10.\n"))
    if N2 < 10 and N2 > 1000000000:
        print("enter a number between 2-10 digits.\n")
    else:
        P = N2
        break
        
while True:
    N1 = int(input("Enter a number between 1 and 5.\n"))
    if N1 > 5 and N1 < 1:
        print("enter a number between 1-5 digits")
    elif N2 == 10 and N1 > 3:
        print("Sorry dude, considering the low value, you'll have to choose a number between 1-3")
    else:
        N = N1
        break
        
while True:
    Shuffle = int(input("Enter amount of shuffles. No greater than 6\n"))
    if int(Shuffle) > 6 and int(Shuffle) < 1:
        print("Shuffles can be no greater than 6 and no lower than 1")
    else:
        S = Shuffle
        break
while True:
    Tries = int(input("Enter amount of tries\n"))
    T = Tries
    break
Pos =  (N * P - 1) * N * P - 1
Re = Pos / S
Per = Re / T
print("The possibility of you repeating the same pattern is %", math.floor(Per))