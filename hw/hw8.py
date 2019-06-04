import numpy as np
import math
import random


def q(i):
    print("Question: ", i)


q(1)
n = 100
p = 0.75
size = 1000
binomial = np.random.binomial(n, p, size)
deviation = math.sqrt(p*(1-p)/n)
mean = n * p
total = 0
for i in binomial:
    if i > (mean + deviation * 2):
        total += 1

print("total 2 standard deviations above mean: ", total)

q(2)


def guess(n):
    r = random.randrange(0, n)
    inp = int(input("enter your guess, 0-" + str(n) + ": "))
    if(inp > r):
        print("too high")
    else:
        print("too low")


guess(100)


def approxPi(n):
    hits = 0
    for i in range(n):
        point = random.random() * 4
        if(point < math.pi):
            hits += 1
    print((hits * 4) / n)


approxPi(100000)


def week():
    days = {
        "Mo": "Monday", "Tu": "Tuesday", "We": "Wednesday", "Th": "Thursday",
        "Fr": "Friday", "Sa": "Saturday", "Su": "Sunday"
    }
    inp = input("Enter Day abbreviation: ")
    if inp in days:
        print(days[inp])


week()
q(3)

year_populations = [8.89, 10.16, 12.0, 13.9, 15.91, 17.93, 20.07, 22.71, 25.97, 29.0, 32.53, 36.07]
out = []
out_2 = []
for i in range(len(year_populations) - 1):
    out.append(year_populations[i + 1] / year_populations[i])
    m = year_populations[i + 1] - year_populations[i]
    out_2.append(m / year_populations[i])
print(out)
print(out_2)

initial_amount = 16
decline = 0.25

for i in range(100):
    initial_amount = initial_amount * decline
    if initial_amount < 0.1:
        print("after ", i, "hours drug is undetectable")
        break
