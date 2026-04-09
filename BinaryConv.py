import threading


def BinConv(n):
    binary = "" 
    n = int(n)
    while int(n) > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    print( binary) if binary != "" else print ("0")

n1 = int(input("Enter a possitive decimal num to convert: "))
bConv = threading.Thread(target=BinConv, args=(n1,))
bConv.start()

# n2 = int(input("Enter a possitive decimal num to convert: "))
# bConv = BinConv((n2,))
# bConv.start()
# n3 = int(input("Enter a possitive decimal num to convert: "))
# bConv = BinConv((n3,))
# bConv.start()
# n4 = int(input("Enter a possitive decimal num to convert: "))
# bConv = BinConv((n4,))
# bConv.start()
