# Unit 1.1 Assignment Code
# Figure out the wrong doings in this code!

'''
1 Point - A, E, I, L, N, O, R, S, T and U.
2 Points - D and G.
3 Points - B, C, M and P.
4 Points - F, H, V, W and Y.
5 Points - K.
8 Points - J and X.
10 Points - Q and Z.
'''

# Scrabble Point Calculator

# input
#shouldnt been an int
word = int(input('Enter a word: ' #Missing a bracket Here

if len(word) == 0:
    print('Illegal input.')
    word = int(input('Enter a word: ' #Missing another bracket
#this if doenst make sense for its purpose, a
#While len(word) == 0 
#would make much more sense, as it would continually checl until its a valid input

# processing
s = 0
#this shouldnt be a range, this should just be for character in word:
for character in range(word):
    if character == 'A':
        s += 1
    if character == 'E':
        s += 1
    if character == 'I':
        s += 1
    if character == 'L':
        s += 1
    if character == 'N':
        s += 1
    if character == 'O':
        s += 1
    if character == 'R':
        s += 1
    if character == 'S':
        s += 1
    if character == 'T':
        s += 1
    if character == 'U':
        s += 1
        #ALL of these 1 point letters could be put into a if character in ""
    elif character in 'DG'
        s += 2
    elif character in 'BCMP':
        s += 3
    elif character in 'FHVWXY':
        s = 4
    elif character in 'JX':
        s += 8
    elif character in 'QZ':
        s += 10
    else:
        s += 5
# end of for
print('Score is' s)
#missing a comma between the string and score