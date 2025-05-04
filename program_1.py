# print 5 rows and 5 col of # using nested loops taking user input

rows = int(input("Enter the number of row = "))
col = int(input("Enter the number of col = "))
symbol = input("Enter the symbol you want to print = ")

for i in range(rows):
    for j in range(col):
        print(symbol, end=" ")
    print()

