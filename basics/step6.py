for i in range(5):
    print(i)

for i in range(1,11,2):
    print(i)


count = 0

while count<3:
    print("count is", count)
    count+=1

for n in range(10):
     if n == 3:
         continue
     if n == 7:
          break 
     print(n)
