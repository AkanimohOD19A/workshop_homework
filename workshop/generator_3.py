# !pip install duckdb

import duckdb
import pandas as pd

con = duckdb.connect(database=':memory:', read_only=False)

## 1st Gen
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

df1 = pd.DataFrame(people_1())
con.register('people', df1)

sum_age_1 = con.execute("SELECT SUM(Age) FROM people").fetchall()[0][0]
print(f"Sum of ages from first generator: {sum_age_1}")

## 2nd Gen
def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

df2 = pd.DataFrame(people_2())
con.register('people', pd.concat([df1, df2]))

## Question III
sum_age_total = con.execute("SELECT SUM(Age) FROM people").fetchall()[0][0]
print(f"Sum of ages from both generators: {sum_age_total}")


## Merge Generators
def generator3(limit):
    gen1 = people_1(limit)
    gen2 = people_2(limit)
    return ({**d, "output": o} for o, d in zip(gen1, gen2))

def sum_of_ages(limit):
    gen3 = generator3(limit)
    total = 0
    for person in gen3:
        total += person["age"]
    return total

sum_of_ages(13)
# Output: 241
