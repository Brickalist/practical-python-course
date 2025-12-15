# bounce.py
#
# Exercise 1.5
fallHeight = 100

for _ in range(10):
    fallHeight -= fallHeight * 0.4
    print(round(fallHeight,4))
