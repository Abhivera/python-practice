fruits = ["apple","banana","cherry"]

fruits.append("mango")

fruits.remove("banana")

fruits[0]="grape"

print(fruits, len(fruits))

for f in fruits:
    print(f)


nums = [5,2,9,1]

nums.sort()

print(nums,sum(nums),max(nums),min(nums))


point = (3,4)

x,y = point

tags = {"a","b","a"}

print(tags)

person = {"name":"Asha","age":25}

person["city"] = "Bengaluru"

print(person["name"],person.get("phone","none"))


print(person.items())

for key,value in person.items():
    print(key,"=",value)


squares = [n**2 for n in nums]
print(squares)

evens =[n for n in range(20) if n%2==0]

print(evens)