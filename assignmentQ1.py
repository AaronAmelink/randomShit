location = int(input(""))
instructions = input("")

for x in instructions:
    if x == "G":
        location += 3
    elif x == "S":
        break
    elif x == "J":
        location += 5
    elif x  == "B":
        location -= 4
print(location)