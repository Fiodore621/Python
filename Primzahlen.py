# primes = []
for num in range(2, 10001):
    prime = True
    for numcheck in range(2, num):
        if num % numcheck == 0:
            prime = False
            break
        else:
            prime = True
    # if prime == True:
    #     primes.append(num)
# print(primes)
