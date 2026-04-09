
def checkIfPalindrome(strNum):
    if strNum[2] == strNum[0]:
        return True
    else:
        return False

def checkN_DigPalindrome (strNum):
    if strNum[::] == strNum[::-1]:
        return True
    else:
        return False

lstPalindrome = []

for i in range(100, 1001, 1):
    if checkIfPalindrome (str(i)):
        lstPalindrome.append(i)
print (lstPalindrome)
lstPalindrome.clear()

for i in range(10000, 20000, 1):
    if checkN_DigPalindrome(str(i)):
        lstPalindrome.append(i)
print (lstPalindrome)
