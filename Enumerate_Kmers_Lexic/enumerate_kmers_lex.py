"""
.
"""

# input
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
k = 3

# compute
kmers = alphabet[:]
for _ in range(k-1):
    
    new_kmers = []
    for kmer in kmers:
        for char in alphabet:
            new_kmers.append(kmer+char)
    kmers = new_kmers[:]

# out
print("\n".join(kmers))