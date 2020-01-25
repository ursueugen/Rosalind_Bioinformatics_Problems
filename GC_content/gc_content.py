fasta = "GC_content/rosalind_gc.txt"

# read all sequences
seqs = {}
with open(fasta, 'r') as f:
    for line in f:
        if line[0] == '>':
            seqid = line[1:-1]
            seqs[seqid] = ''
        else:
            seqs[seqid] += line.split('\n')[0]

print(seqs)

def gc_content(seq):
    return ( seq.count("C") + seq.count("G") ) / float(len(seq))

gcs = {}
mx = 0
max_id = None
for key, seq in seqs.items():
    gcs[key] = gc_content(seq)
    if gcs[key] > mx:
        max_id = key
        mx = gcs[max_id]

print("{}\n{:08.6f}".format(max_id, gcs[max_id]*100))