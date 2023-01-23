import urllib

def find_ngly(prot):
    l=len(prot)
    locs=[]
    for i in range(0,l-3):
        if prot[i]=="N" and (prot[i+2]=="S" or prot[i+2]=="T") and prot[i+1]!="P" and prot[i+3]!="P":
            locs.append(str(i+1))

    return locs

def run_ngly(up_id):
    protein_url="http://www.uniprot.org/uniprot/"+up_id+".fasta"
    f=urllib.urlopen(protein_url)
    protein_fasta=f.read()
    protein_fasta=protein_fasta.split("\n")
    protein_seq="".join(protein_fasta[1:])
    glys=find_ngly(protein_seq)
    if len(glys)>0:
        print (up_id)
        print (" ".join(glys))


f=open("rosalind_mprt (2).txt")
up_ids=f.readlines()
f.close()

up_new=[i[:-1] for i in up_ids[:-1]]
up_new.append(up_ids[-1])

for i in up_new:
    run_ngly(i)