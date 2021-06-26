i = True

def isprime(num):
    for i in range(2,num):
        if not(num%i):
            return False
        return True

while i == True:
    num = int(input('input a num or type 12 to stop: '))
    if num == 12:
        break
    if isprime(num):
            print(num)
    
