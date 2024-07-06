animals = ['cat', 'dog', 'hamster', 'python']
print(animals)

while "dog" in animals:
    animals.remove("dog")

if "bull" not in animals:
    animals.append("bull")
   

print(animals)
