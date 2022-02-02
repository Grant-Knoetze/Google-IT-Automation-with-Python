# Iterate through a sequence

animals = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))

# Enumerate through a sequence

winners = ["Lion", "Tiger", "Elephant", "Giraffe", "Zebra"]
for i, winner in enumerate(winners):
    print("{} is the {} winner".format(winner, i+1))


