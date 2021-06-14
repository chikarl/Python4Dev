string = 'Python 4 dev task 1 '
string = string.split()
num = []
def ifNumber(x):
    for i in string:
        if i.isdigit():
            num.append(int(i))
    return num
print(ifNumber(string))
def isPrime(n):
    for i in range(2,n):
        if not(n%i):
            return False
    return True

def factorial(x):
    if x==1:
        return 1
    return x* factorial(x-1)
if num == []:
    print ('the user there is no calculations available')
else:
    for i in num:
        if isPrime(i):
            print(f'{i} is prime')
        else:
            print(f'{factorial(i)} is the Factorial of {i}')

