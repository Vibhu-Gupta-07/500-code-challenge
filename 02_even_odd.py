# method 1 
# using brute force 

num = int(input("Enter the number"))

if(num%2==0):
    print('Even')
else:
    print('Odd')

# method 2 
# using ternary operator

num = 6 
print("Even") if num%2==0 else print("ood")


# method 3
# using bitwise operator

def isEven(num):
    return not num&1

if __name__ == "__main__":
    num = int(input("Enter the value"))
    if isEven(num):
        print('Even')
    else:
        print('Odd')
