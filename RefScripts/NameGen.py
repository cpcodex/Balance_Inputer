from faker import Faker

fake = Faker()
names = [fake.name() for num in range(100000)]
first_names = [name.split()[0] for name in names]

num = 0
for name in names:
    num += 1
    name.split()[0]
    print(f"{num}: {name}")
