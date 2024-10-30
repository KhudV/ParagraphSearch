path = 'myCounter.txt'

def counter():
    q = 0
    with open(path, 'r') as file:
        s = file.readline()
        q = int(s)
    with open(path, 'w') as file:
        file.write(str(q+1) + '\n')
    return q
