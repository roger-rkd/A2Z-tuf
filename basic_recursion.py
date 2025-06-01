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
        
# print_1_to_n(1,5)

def print_n_to_1(n,i):
    if i<=n:
        print(n)
        print_n_to_1(n-1,i)

# print_n_to_1(5,1)

def sum_of_first_n_numbers(i,n,c):
    if i<=n:
        c+=i
        sum_of_first_n_numbers(i+1,n,c) # handling c in the main function call
    else:
        print("Sum :", c)

# sum_of_first_n_numbers(1,10,0) # initializing c as 0

def factorial(n,i,c):
    if i<=n:
        c*=i
        factorial(n,i+1,c)
    else:
        print("Factorial :",c)

# factorial(5,1,1)

def reverse_array(arr, left_position, right_position): # revise
    if right_position>=left_position: # base condition to check when the right postion <= left position
        arr[left_position],arr[right_position]=arr[right_position],arr[left_position] # swapping the values of both left and right postions
        reverse_array(arr,left_position+1,right_position-1) # updating the positions
    else:
        print(arr)

reverse_array([10,20,30,40],0,3)