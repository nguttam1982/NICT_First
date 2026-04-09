import threading
import time

class S1 (threading.Thread):
    
    def run(self):
        for i in range(1, 11):
            print  (f"3 x {i} = {3 * i}")
            time.sleep(1)


s = S1()
s.start()
