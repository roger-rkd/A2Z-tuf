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

check_palindrome(10321)

