import time
minuto = 0
segundo = 0

while segundo <= 59 :
    print(f"{minuto:02}:{segundo:02}")
    time.sleep(1)  
    
    segundo += 1

