import random
with open('sowpods.txt','r') as f:
    lines=f.read()
    list = lines.split()
    print(random.choice(list))
