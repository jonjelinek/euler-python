# Lexicographic permutations
from itertools import permutations

perms = permutations('0123456789')
# Print the millionth permutation from the sorted list of permutations
print(''.join(sorted(list(perms))[1000000 - 1]))

