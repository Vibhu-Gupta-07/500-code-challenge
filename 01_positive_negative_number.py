# Method 1
# using Burte force 

num = 15

if num > 0:
    print('postive')

elif num < 0:
    print('negative')

else:
    print('Zero')

# Method 2
# using nested if else statement

num = 15 
if num >= 0:
    if num == 0:
        print('Zero')
    else:
        print('Positive') 

else: 
    print('negative')

# Method 3
# Using ternary operator 

num = -3
print("Positive" if num >=0 else "negative")