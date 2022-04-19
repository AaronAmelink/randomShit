"""# s2 groups
'''
3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L


x = int(input())
first = [input().split() for _ in range(x)]

y = int(input())
second = [input().split()  for _ in range(y)]

z = int(input())
third = [set(input().split()) for _ in range(z))]
'''

#x = int(input())
#first = [input().split() for _ in range(x)]
#print(first)
first = [['A', 'B'], ['G', 'L'], ['J', 'K']]
second = [['D', 'F'], ['J', 'K']]
third = [set("ACG"), set("BDF"), set("EHI"), set("JKL")]
#z = int(input())
#third = [set(input().split()) for _ in range(z)]

violations = 0

together = {} # must be together
for s1, s2 in first:
    if s1 not in together:
        together[s1] = {s2}
    else:
        together[s1].add(s2)
    
separate = {} # must be separate
for s1, s2 in second:
    if s1 not in separate:
        separate[s1] = {s2}
    else:
        separate[s1].add(s2)

print(first)
for group in third:
    print(group)
    for member in group:
        print(member)
        # checking if the needed people are together
        if member in together:
            diff = together[member] - group
            print(diff)
            violations += len(diff)

        # check if ppl are separated
        if member in separate:
            inter = group & separate[member]
            violations += len(inter)

print(violations)"""

together = ["Aaron", "John"]
amogus = {
    "Aaron" : "John", 
}
amogus["Aaron"].add("Marcus")

for x in amogus:
    if x in together:
        print(x)

print(amogus)