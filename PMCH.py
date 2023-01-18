from math import factorial

seq = 'GUCCUCUCCGGCAGCUGCCAGGAGCGGAAUACAUAAAAGGCGUAGCAUUUUUUAGUUACCCCCUGGAGUCAUAG'
match = factorial(seq.count('U')) * factorial(seq.count('G'))

print(match)