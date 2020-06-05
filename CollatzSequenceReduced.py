import time

def isInt(nInput):
    try:
        int(nInput)
        return True
    except ValueError:
        return False
    
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(number * 3 + 1)
        return number * 3 + 1

n = input('Please enter a number:')
while n != 1:
    if isInt(n) == True:
        n = collatz(int(n))
        time.sleep(0.1)
    else:
        n = input('Please enter an integer;')
