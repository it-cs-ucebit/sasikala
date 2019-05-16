n = input ("Enter a number : ")
n = int(n)
e = input ("Enter an exponent : ")
e = int(e)
r = n
for i in range (1,e):
    r = n * r
print(r)
