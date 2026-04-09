text = input ("Give an input string: ")
text = text.upper()


ascii_values = [ord(char) for char in text]
print(ascii_values)

k = 0
bInOrder = True

while k < len(ascii_values) - 1:
    if ascii_values[k] == 32:         ### Space character ignored
        continue 
    if ascii_values[k] > ascii_values[k+1]:
        bInOrder = False
        break
    k += 1
if bInOrder:
    print ("String is in alphabetical order")
else:
    print ("String is not in alphabetical order")

print ("Using for loop:")
print ("")

bInOrder = True

for i in range(len(text) - 1):
    if text[i] > text[i + 1]:
        bInOrder = False
        print ("String is not in alphabetical order")
if bInOrder:
    print ("String is in alphabetical order")


print ("Using while loop:")
print ("")

while k < len(text) - 1:
    if text[k] == 32:         ### Space character ignored
        continue 
    if text[k] > text[k+1]:
        print ("String is not in alphabetical order")
        break
else:
    print ("String is in alphabetical order") 
