'''
Problem 32 - FLAME Game
- Write a program which implements FLAME.
- Have the user input two names.
- Display each step of the game as illustrated in the link above.
'''

# input names
def input_name(string):
    for i in string:
        if i.isalpha() == False:
            return False
    else:
        return True

arrow = "<--"
print("Welcome to the FLAME (friends, lovers, affectionate, marriage, enemies) game. Input two names to find out these two people's compatibility.\n")

# repeatability
while True:
    flame = ['Friends ', 'Lovers ', 'Affectionate ', 'Married ', 'Enemies ']
    names = [[], []]
    
    # get first name input
    while True:
        name0 = input("Please provide the first name.\n").replace(" ","").lower()
        if input_name(name0):
            names[0] = [x for x in name0]
            break
        else:
            print("The name you entered is not valid. Please try again.\n")

    # get second name input
    while True:
        name1 = input("Please provide the second name.\n").replace(" ","").lower()
        if input_name(name1):
            names[1] = [x for x in name1]
            break
        else:
            print("The name you entered is not valid. Please try again.\n")
    
    # compare letters
    common = []
    for i in names[0]:
        for j in names[1]:
            if i == j and i not in common:
                common.append(j)
    for i in range(2):
        for j in names[i]:
            if j in common:
                names[i][names[i].index(j)] = "_"
        if names[i][0] != "_":
            names[i][0] = names[i][0].upper()

    if len(common) > 0:
        print("\n" + name0.capitalize() + " and " + name1.capitalize() + " have the letters " + str(common) + " in common, leaving:",
              "\n" + str(" ".join(names[0])) + " and " + str(" ".join(names[1])))
    else:
        print("\n" + name0.capitalize() + " and " + name1.capitalize() + " have no letters in common!")
    
    # iterate through remaining letters and get FLAME result
    count = 0
    for i in range(2):
        for j in names[i]:
            if j != "_":
                count += 1
    count %= len(flame)
    
    # print result
    print("\nThese two people will be...")
    if count == 0:
        flame[4] += arrow
    for i in range(len(flame)):
        if count != 0 and i == count-1:
            flame[i] += arrow
        print(flame[i])

    # play again?
    if input("\nWould you like to play again? 'Y' for yes or 'N' for no.\n").lower().replace(" ", "") == 'n':
        print("Thanks for playing!")
        break
