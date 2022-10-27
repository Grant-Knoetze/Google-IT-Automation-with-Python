# Create a list

animals = ["Giraffe", "Zebra", "Lion", "Leopard"]

animals_upper = (animal.upper()for animal in animals)

for animal in animals_upper:
    print(animal)


