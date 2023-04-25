import sys
import time
prog=0
for x in range(10):
    prog=x*u"\u267F"
    prog1=(10-x)*u"\u26BD"
    progress=prog+prog1
    sys.stdout.flush()
    sys.stdout.write('\rProgress: %3s %%' %progress)
    time.sleep(0.1)
