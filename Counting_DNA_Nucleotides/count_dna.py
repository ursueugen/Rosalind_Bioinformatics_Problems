BASES = ['A','C','G','T']

with open("rosalind_dna.txt", 'r') as f:
    dna = f.read()

counts = []
for b in BASES:
    counts.append(str(dna.count(b)))

print(" ".join(counts))
