year=2032
if (year%400==0) or (year%100!=0 and year%4==0):
    print(year,"lear year")
else:
    print(year,"not a leap year")