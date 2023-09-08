import random

def computer_Guess(x):
    low = 1
    high = x
    corr = ""
    
    while corr != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        corr = input(f"{guess}, If i guess High (h), if i guess low (l), if i guess correct (c):  ")

        if corr == "h":
            high = guess - 1 

        elif corr == "l":
            low = guess + 1

    print(f"Hurray , i guess the right number {guess}")

computer_Guess(100)