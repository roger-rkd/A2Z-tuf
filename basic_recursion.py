def print_n_numbers(n):
    if n<=5:
        print(n)
        n+=1
        print_n_numbers(n) # recursive function

# print_n_numbers(0)

def print_name_n_times(n):
    if n<=5:
        print("Mahadev")
        n+=1
        print_name_n_times(n) # recursive function

# print_name_n_times(1)

def print_1_to_n(i,n):
    if i<=n:
        print(i)
        print_1_to_n(i+1,n)
        
print_1_to_n(1,5)