# Problem 17: Seat Reservation
 # Create a simple seat reservation program
 # Create a list that would store dashes '-' as a symbol that the seat is still available to take.
 # Define a function that would loop over the list and print out the seats horizontally or in a 3 x 3 position. 
 # Define a second function that would check if the seats are occupied. This should check if the list contains "X" in each element, which is the symbol that we will use if the seat is taken that you will store in a variable.
 # If the variable is equal to 9 (the total number of seats), return True (and break from the loop), and False if not.
 # Create a loop that would have to (1) ask the user for the number of seat he would want to reserve, (2) print out the chairs, (3) check if all the seats are occupied and (4) ask the user now if he/she wants to reserve again.

# Original: 13 December 2020

# print seating layout
def print_grid(grid):
    print(grid_col)
    for i in range(len(grid)):
        print(grid_row[i], grid[i])

# create seating list
grid = [['-' for x in range(3)] for y in range(3)]
grid_col = "    A    B    C"
grid_row = [1, 2, 3]

while True:
    # get input and make sure input is valid: A1 to C3 and not taken
    print("The current seats are available:")
    print_grid(grid)
    seat = input("What seat would you like to reserve?\n").upper().replace(" ","")
    try:
        row, col = int(seat[0]), seat[1]
        if (seat[1] in grid_col and int(seat[0]) in grid_row and len(seat)==2):
            if grid[row-1][((grid_col.index(col)+1)//5)-1] == "-":
                print("Congrats! You have reserved " + seat + ":")
                grid[row-1][((grid_col.index(col)+1)//5)-1] = "X"
                print_grid(grid)
            else:
                print("The seat you specified has already been reserved.\n")
                continue
        else:
            raise ValueError
    except: 
        print("Please enter a valid seat in the format [row][column], such as: 2A.\n")
        continue

    # if all seats are reserved
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "X":
                count+=1
    if count == 9:
        print("All of the seats are taken!")
        break
    
    # continue?
    if input("\nWould you like to reserve another seat? 'Y' or 'N'\n").lower().replace(" ","")=="n":
        break
