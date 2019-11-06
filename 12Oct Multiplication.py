# 12 Oct 2019
# Multiplication Tables

n = int(input("I will generate a multiplication table. Give me a number and I'll make a table with that many rows and columns. \n"))

def table(n):
    table = [[" "]]
    inc = 1
    # Fill in first row (unique)
    for x in range(1,n+1):
        table[0].append(str(x))
    # Add and populate new rows
    for y in range(1,n+1):
        table.append([str(y)])
        for z in range(1,n+1):
            table[y].append(str(y*z))
    space = len(table[n][n])
    for row in range(n+1):
        for cell in range(n+1):
            while len(table[row][cell]) < space:
                table[row][cell] = " " + table[row][cell]
    return(table)

for row in table(n):
    print(row)

