# count digits

def count_digits(n):
    c=0
    while(n>0):
        n=n//10
        c+=1

    print(c)


# reverse number

def reverse_number(n):
    reverse = 0
    while(n>0):
        last_digit = n%10
        reverse = reverse*10 + last_digit
        n=n//10

    print(reverse)

reverse_number(1009)
