alignment = "Counting_Point_Mutations/rosalind_hamm.txt"

# read
with open(alignment, 'r') as f:
    seqs = []
    for line in f:
        seqs.append(line.split('\n')[0])
    seq1, seq2 = seqs

# count
mutations = sum(map(lambda i: seq1[i] != seq2[i], range(len(seq1))))
print(mutations)