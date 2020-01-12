COMPLEMENT = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
FILENAME = 'rosalind_revc.txt'

with open(FILENAME, 'r') as f:
    dna = f.read()[:-1]

reverse_complement = "".join(list(map(lambda x: COMPLEMENT[x], dna)))[::-1]
print(reverse_complement)
