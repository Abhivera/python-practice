def greet(name):
    return f"Hello, {name}"

print(greet("Ravi"))


def add(a,b=10):
    return a+b

print(add(5),add(5,3),add(a=1,b=2))

def stats(numbers):
    return min(numbers),max(numbers),sum(numbers)/len(numbers)

lo,hi,avg = stats([4,8,12])

print(lo,hi,avg)