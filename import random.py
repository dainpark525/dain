import random

a=random.randint(1,32)
print(a)

fruits=['사과','오랜지','수박']
b=random.choice(fruits)
print(b)

random.shuffle(fruits)
print(fruits)