def print_n_numbers(n):
    if n<=5:
        print(n)
        n+=1
        print_n_numbers(n) # recursive function

print_n_numbers(0)
