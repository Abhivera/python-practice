
score = int(input("Score: "))

if score >=90:
    print("A")

elif score >=75:
    print("B")

elif score >=50:
    print("Pass")

else:
    print("Fail")

age, has_ticket = 20 , True
if age>=18 and has_ticket:
    print("Enter")