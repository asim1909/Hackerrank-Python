from datetime import datetime

def delta(d1,d2):
    f= '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.strptime(d1, f) 
    d2 = datetime.strptime(d2, f) 
    diff = (d2-d1).total_seconds()  
    return abs(int(diff))

for _ in range(int(input())):
    print(delta(input(), input()))
