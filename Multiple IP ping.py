import os
import time
from pythonping import ping

while True:
    with open('ip-source.txt') as file:
        dump =file.read()
        dump =dump.splitlines()

    for ip in dump:
        
        os.system('cls')
        print("pinging now:",ip)
        print('-'*20,'>'*5)
        
        ping(ip, verbose=True)
        print('-'*60)
        
        time.sleep(5)
   
