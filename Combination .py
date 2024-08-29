from itertools import permutations

def generate_permutations(number):
    # Convert the number to a string to get its digits
    digits = str(number)
    # Generate all permutations of the digits
    perm = permutations(digits)
    # Convert permutations back to integers
    perm_numbers = [int(''.join(p)) for p in perm]
    # Remove duplicates by converting to a set and then back to a list
    unique_perm_numbers = list(set(perm_numbers))
    return unique_perm_numbers

# User input
number = int(input("Enter the number: "))

# Generate permutations
permutations_list = generate_permutations(number)

# Print the permutations
print("All possible combinations by swapping digits:", permutations_list)

# Print the count of generated permutations
print("Total number of unique permutations:", len(permutations_list))
