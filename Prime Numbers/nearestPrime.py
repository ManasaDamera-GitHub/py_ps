number = int(input("enter number: "))

# to find smaller and larger
smaller = number - 1
larger = number + 1

# smaller prime
while smaller > 1:
    for i in range(2,smaller):
        if smaller % i == 0:
            break
    else:
        break
    smaller -= 1

# larger prime
while True:
    for i in range(2,larger):
        if larger % i == 0:
            break
    else:
        
        break
    larger += 1

if (number - smaller) == (larger - number ):
   res= f"{smaller},{larger} both are primes"
elif (number - smaller) < (larger - number ):
    res=f"{smaller} is nearest smaller"
else:
    res=f"{larger} is largest prime"

print(res)