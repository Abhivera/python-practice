with open("notes.txt","w") as f:
    f.write("line one \n")
    f.write("line two \n")

with open("notes.txt") as f:
    for line in f:
        print(line.strip())

try:
    n = int(input("Number: "))
    print(10/n)
except ValueError:
    print("That was not a number")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
finally:
    print("Done")
