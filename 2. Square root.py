"""def newtonSqrt(n, howmany):
    approx = 0.5 * n
    for i in range(howmany):
        betterapprox = 0.5 * (approx + n/ approx)
        approx = betterapprox
    return betterapprox
print(newtonSqrt(10, 3))
print(newtonSqrt(10, 5))
print(newtonSqrt(10, 10))"""

n = int(input("Enter a number"))
howmany = int(input("Enter another number"))
approx = 0.5 * n
for i in range(howmany):
    betterapprox = 0.5 *(approx + n/approx)
    approx = betterapprox
print("The square root of a number is:", betterapprox)
            


