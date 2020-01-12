with open("rosalind_rna.txt", 'r') as f:
    dna = f.read()

rna = "".join(list(map(lambda x: 'U' if x=='T' else x, dna)))
print(rna)
