source = [5, 4, 3, 2, 1]
dest = []
aux = []

def Hanoi(disk, source, dest, aux):
    if disk == 1:
        dest.append(disk)
        source.pop(source.index(1))
    else:
        Hanoi(disk - 1, source, aux, dest)
        dest.append(disk)
        source.pop(source.index(disk))
        Hanoi(disk-1, aux, dest, source)


Hanoi(source[0], source, dest, aux)

print(dest)