# s2 groups

x = int(input()) # gets number of people that have to be together
first = [input().split() for _ in range(x)] # gets all name pairs, splits it based on the space, and puts it into a list of lists
# ex: [["Jonh", "Mark"], ["Aaron"], ["Carol"]]

y = int(input()) #  #gets number of people that cant be together
second = [input().split()  for _ in range(y)] # gets all name pairs, and splits it the same as above

z = int(input()) # gets number of actual groups
third = [set(input().split()) for _ in range(z)] # gets all groups, and puts it into a list of sets
print(third)
#third is a list of sets
# ex: [{'"Chi", "Deborah", "Francis"}, {"Aaron", "Park", "Carol"}]

#First is the list that must be together, second cant be together, and third is the actual groups.

violations = 0 # represents the number of violations made

together = {} # must be togethers
for s1, s2 in first: # iterates through each list of list, and creates a dictionary based on that. s1 becomes the key and s2 the value
    if s1 not in together: # if s1 key not already made
        together[s1] = {s2} # creates a Key of s1, and a set containing s2
    else:
        together[s1].add(s2) # if s1 is already a Key, add s2 to the set that is its value

separate = {} # must be separate
for s1, s2 in second: # does the same as above, except with the "cannot be together" restriction
    if s1 not in separate:
        separate[s1] = {s2} # create a key of s1, and a set containing s2
    else:
        separate[s1].add(s2) # if s1 is already a key, add s2 to the preexisting set

for group in third: #iterates through each actual group
    for member in group: # iterates through each member in said group

        # checking if the needed people are together
        if member in together: # if the member is a key in together
            diff = together[member] - group # checks for any values that are in both the together[member] value set and group, and creates a new set that has names that are in the together[member] value set but not in group, if the diff set is not empty, it has violations
            violations += len(diff) # length of diff is added to violation, as that is the number of violations that are made.

#example of above:
#group = [["Aaron", "John", "Carol"]]
#together = {
#    "Aaron" : {"Marcus", "Kevin"}
#}
#
#in this example, nothing would be removed from the Aaron Key, so then len(diff) would be 2, and added to violations

#inter

        # check if ppl are separated
        if member in separate:
            inter = group & separate[member] # looks for values that are in both group, and the separate[member] value set, which are a violation, and sets it equal to inter, 
#ex:
#Seperate = {
# "Aaron" : "Marcus"
# }
#group = ["Aaron", "John"]
# inter = group & seperate["Aaron"]
#inter would be nothing, as no values are in both. if Marcus was John instead, inter would be John.
            violations += len(inter)
            #simply adds the length of inter to violations, as that is the number of violations made

print(violations)
#prints the number of total violations