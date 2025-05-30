#     *
#    ***
#   *****
#  *******
# *********


def pattern7(n):
    for i in range(0,n):

        # for space
        for j in range(n-i-1,0,-1):
            print(" ", end="")

        # for *
        for k in range(0,i*2+1):
            print("*",end="")

        # for space
        for l in range(n-i-1,0,-1):
            print(" ", end="")

        # for new line
        print('\n')

def pattern8(n):
    for i in range(0,n):

            # for space
            for j in range(0,i):
                print(" ", end="")

            # for *
            for k in range(0,2*n-(2*i+1)): # building logic for the astric is the real game, lessssssgoooooooooo
                print("*",end="")

            # for space
            for l in range(0,i):
                print(" ", end="")

            # for new line
            print('\n')

def pattern9(n):
    pattern7(n)
    pattern8(n)

def pattern10(n):
    # code for the first half
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print('\n')

    # code for the second half
    for i in range(0,n):
        for j in range(n-1,i,-1):
            print("*", end="")
        print('\n')

def pattern11(n):
    
    
    for i in range(0,n):
        start = 0
        if i%2==0:
            start = 1
        for j in range(0,i+1):
                print(start, end="")
                start = 1 - start # the main logic
        print('\n')
            
def pattern12(n):
    space = 2*(n-1)  # real logic
    for i in range(0,n):
        
        for j in range(0,i+1):
            print(j+1,end="")

        for k in range(0,space):
            print(" ", end="")

        for l in range(i+1,0,-1):
            print(l,end="")
        print('\n')
        space-=2 # real logic
            
def pattern13(n):
    c=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(c,end="")
            c+=1
        print('\n')
        
def pattern14(n):
    for i in range(0,n):
        row=""
        for j in range(i+1):
            row += chr(ord('A')+j) # the real logic ---------> GAME OF <CHR(ORD('CHAR'))>
        print(row)

def pattern15(n):
    for i in range(n+1,0,-1):
        row=""
        for j in range(i): # here range(i) mean the loop is running for i times
            row += chr(ord('A')+j)
        print(row)

def pattern16(n): 
    for i in range(1,n+1):
        row=""
        for j in range(i):
            row+=chr(ord('A')+(i-1))
        print(row)

def pattern17(n):
    for i in range(0,n):

        # for front spaces
        for j in range(n,i,-1):
            print(" ",end="")

        # for alphabets <------------- REAL LOGIC
        
        
        ch = 'A'
        breakpoint = (2 * i + 1) // 2
        for j in range(1, 2 * i + 2):  
            print(ch, end="")
            if j <= breakpoint:
                ch = chr(ord(ch) + 1)  # Increment character
            else:
                ch = chr(ord(ch) - 1)  # Decrement character
            

        # for rear spaces
        for j in range(n,i,-1):
            print(" ",end="")

        print('\n')
        
def pattern18(n):
    for i in range(n):
        ch = chr(ord('A')+(n-1)-i)
        for j in range(0,i+1):
            print(ch,end="")
            ch = chr(ord(ch)+1)
        print('\n')

def pattern19(n):
    for i in range(n):
        # for front *
        for j in range(n-i,0,-1):
            print("*", end="")

        # for spaces
        for j in range(0,i*2):
            print(" ",end="")

        # for rear *
        for j in range(0,n-i):
            print("*", end="")

        print('\n')

        # reversing the same pattern ----------------> WAS STUCK IN INDENTATION
    for i in range(n):
            # for front *
        for j in range(i+1):
            print("*", end="")

        # for spaces
        for j in range(2*(n-(i+1)),0,-1):
            print(" ",end="")

        # for rear *
        for j in range(i+1):
            print("*", end="")

        print('\n')

pattern19(5)
            






    

