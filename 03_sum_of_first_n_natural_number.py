# Method 1
# using loop 

n = int(input("Enter the number: "))
sum = 0
for i in range (n+1):
    sum+=i
    
print(sum)


# method 2
# using formula fo the sum of Nth number

print(int(n*(n+1)/2))

print((n+1)/2)

# Method 3
# using recursion 

def getSum(n):
    if n==1:
        return 1
    return n + getSum(n-1)   
n = 5
print(getSum(n)) 