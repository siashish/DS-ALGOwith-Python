# brute force method
def gcd_brute(a,b):
     m = min(a, b)
     for i in reversed(range(m)):
        if i>0 and a%i==0 and b%i==0:
            return i

# Euclid's gcd algorithm
def gcd_euclid(a,b):
    if b==0:
        return a
    else:
        return gcd_euclid(b,a%b)

print(gcd_brute(10,15))
print(gcd_euclid(1000,2000))