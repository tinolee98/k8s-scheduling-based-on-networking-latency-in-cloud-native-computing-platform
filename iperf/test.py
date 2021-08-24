import os
from time import sleep

while(1):
    print('press \'ctrl c\' to kill the process')
    print("measuring network latency")
    os.system("./steps/run.sh")
    print("finish?")
    sleep(2)
