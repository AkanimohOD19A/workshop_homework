def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)
totalSum = sum(generator)

for sqrt_value in generator:
    print(sqrt_value)
    
print(f"Sum: {totalSum}")