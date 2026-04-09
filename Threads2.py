import threading

def power (base, exp):
    result = 1
    for i in range(1, exp + 1):
        result = result * base
    print(result)


t1 = threading.Thread(target=power, args=(3, 4))
t2 = threading.Thread(target=power, args=(2, 4))
t1.start()
t2.start()


def CheckIfPrime(num, x): #ignore second param x, taking it since thread func accepts only tuples
    bPrime = True
    for i in range (2, int(num)):
        if num % i == 0:
            print(f"{num} is not prime.")
            bPrime = False
            break

    if bPrime: 
        print(f"{num} is prime.")
    
t3 = threading.Thread(target=CheckIfPrime, args=(23,1)) 
t4 = threading.Thread(target=CheckIfPrime, args=(12,2))
t3.start()
t4.start()

def findLCM(num1, num2):
    i = 1
    while True:
        if (i % num1 == 0 and i % num2 == 0):
            LCM = i
            break
        i += 1
    print(LCM)

t5 = threading.Thread(target=findLCM, args=(3, 9))
t5.start()

t6 = threading.Thread(target=findLCM, args=(2, 15))
t6.start()
