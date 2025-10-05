
add = lambda x, y: x + y
print("Sum:", add(5, 3))


square = lambda x: x ** 2
print("Square:", square(4))


numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)


doubled = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled)