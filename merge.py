import time


list = "11 8 78 70 76 30 15 14 97 23 36 77 53 9 99 50 29 27 67 4 79 100 52 80 33 2 72 65 6 94 95 20 60 34 17 75 69 40 51 22 88 85 55 81 38 31 92 16 68 54 18 25 28 12 74 42 62 57 21 91 66 47 93 43 41 96 10 32 59 98 84 24 3 49 56 35 45 13 26 90 5 58 64 48 1 89 39 7 44 37 46 71 83 82 73 19 87 63 86 61"
list = list.split(" ")
myList = []
for x in list:
    myList.append(int(x))

start_time = time.time()

myList.sort()
print("--- %s seconds ---" % (time.time() - start_time))

list = "11 8 78 70 76 30 15 14 97 23 36 77 53 9 99 50 29 27 67 4 79 100 52 80 33 2 72 65 6 94 95 20 60 34 17 75 69 40 51 22 88 85 55 81 38 31 92 16 68 54 18 25 28 12 74 42 62 57 21 91 66 47 93 43 41 96 10 32 59 98 84 24 3 49 56 35 45 13 26 90 5 58 64 48 1 89 39 7 44 37 46 71 83 82 73 19 87 63 86 61"
list = list.split(" ")
myList = []
for x in list:
    myList.append(int(x))

start_time = time.time()

def merger(x, y):
    sorted = []
    lastX = x[-1]
    lastY = y[-1]
    run = True
    while run:
        if x[0] < y[0]:
            sorted.append(x[0])
            z = x.pop(0)
        else:
            sorted.append(y[0])
            z = y.pop(0)
        if z == lastX:
            run = False
            lastX = True
        elif z == lastY:
            run = False
            lastY = True
    if isinstance(lastX, bool):
        sorted.extend(y)
    elif isinstance(lastY, bool):
        sorted.extend(x)
    return sorted
            


def divider(n):

    le = len(n)

    if le <= 1:
        return n
        
    
    left = n[:le//2]
    right = n[le//2:]

    left = divider(left)
    right = divider(right)
    return merger(left, right)
    

    

dick = divider(myList)
print("--- %s seconds ---" % (time.time() - start_time))