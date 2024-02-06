
def count(array):
    return [len(str(element)) for element in array]

strings = ["lamp", "shade", "light", "good morning"]
integers = [7777, 45, 0, 235]

output_strings = count(strings)
output_integers = count(integers)

print(output_strings)
print(output_integers)
