import random
def func(x,y):
    a = x**2 + y**2 
    if (a <= 1000**2):
        return f"Poniżej {a}"
    else:
        return f"Powyżej: {a}" 

i = 0
while(i < 1000000):
    x = random.randint(-1000,1000)
    y = random.randint(-1000,1000)
    print(func(x,y))
    i+=1
