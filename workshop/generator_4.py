def generator3(limit):
    gen1 = generator1(limit)
    gen2 = generator2(limit)
    return ({**d, "output": o} for o, d in zip(gen1, gen2))

def sum_of_ages(limit):
    gen3 = generator3(limit)
    total = 0
    for person in gen3:
        total += person["age"]
    return total

sum_of_ages(13)