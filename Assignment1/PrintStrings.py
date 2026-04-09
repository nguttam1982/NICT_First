# program using control Structure to print the following pattern

# D
# E E
# C C C  
# B B B B
# A A A A A

strPrint = 'DECBA'
i = 1
for char in strPrint:
    for j in range(0, i):
        print (strPrint[i-1], end=" ")
    i += 1
    print ("")

