def count_digits(n):
    c=0
    while(n>0):
        n=n//10
        c+=1

    print(c)

a = int(input("Enter the number to be counted: "))
count_digits(a)

