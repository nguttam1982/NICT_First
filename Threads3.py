# Find leap year without using modulus or division operators

import threading


class S1 (threading.Thread):
    
    def run(self):
        bLeapYr = False
        yr = int(input("Enter a year: "))
        i = 0
        while i <= yr:
            if i == yr:
                print ("Its a leap year")
                bLeapYr = True
            i += 4
        if not bLeapYr:
            print ("Its not a leap year")



s = S1()
s.start()


