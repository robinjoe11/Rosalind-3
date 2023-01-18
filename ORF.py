def orf(sequence):
    rev_seq = sequence[::-1].replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()
    codon = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
    'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
    }
    prolist = []
    for start in range(len(sequence)-3):
        prosequence = ''
        if codon[sequence[start:start+3]] == 'M':
            for n in range(start,len(sequence),3):
                if sequence[n:n+3] in codon.keys():
                    prosequence += codon[sequence[n:n+3]]
                    if codon[sequence[n:n+3]] == '':
                        if prosequence != '':
                            prolist.append(prosequence)
                        break
    for start in range(len(rev_seq)-3):
        prosequence = ''
        if codon[rev_seq[start:start+3]] == 'M':
            for n in range(start,len(rev_seq),3):
                if rev_seq[n:n+3] in codon.keys():
                    prosequence += codon[rev_seq[n:n+3]]
                    if codon[rev_seq[n:n+3]] == '':
                        if prosequence != '':
                            prolist.append(prosequence)
                        break
    return set(prolist)
seqlist = []
stseq = ''
for line in open('rosalind_orf (2).txt'):
    if line[0] == '>':
        if stseq != '':
            seqlist.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seqlist.append(stseq)
proteins = orf(seqlist[0])
for i in proteins:
    print (i)