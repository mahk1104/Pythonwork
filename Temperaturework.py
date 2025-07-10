highest=0

for temperature in range(1,13):
    print("Month " +str(temperature))
    a=int(input("Enter the temperature"))
    if highest<a:
        highest=a
print ("The highest temperature is "+str(highest))

lowest=0

for temperature in range(1,13):
    print("Month " +str(temperature))
    a=int(input("Enter the temperature"))
    if lowest>a:
        lowest=a
print ("The lowest temperature is "+str(lowest))



