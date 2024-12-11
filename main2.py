n = int(input("Enter the number of rows")) #input from user
#outer loop to create each row
for i in range(1,n+1):
    #inner loop is going to display number of stars per row
    for j in range(i):
        #print * with space at the end
        print("/",end="")
        #after each row u need to print a new line
    print() 