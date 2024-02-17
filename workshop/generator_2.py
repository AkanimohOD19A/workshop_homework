def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13
generator = square_root_generator(limit)

last_value = None
for sqrt_value in generator:
    last_value = sqrt_value

print(last_value)

    
