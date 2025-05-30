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

# check palindrome

def check_palindrome(n):
    reverse, copy = 0, n

    while(copy>0):
        last_digit = copy%10
        reverse = reverse*10 + last_digit
        copy=copy//10

    if reverse==n:
        print("palindrome")
    else:
        print("not palindrome")


def hcf(a, b):

    for i in range(1, min(a,b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
        
    print(gcd)

hcf(9,12)


    
