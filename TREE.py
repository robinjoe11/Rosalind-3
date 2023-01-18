
with open("rosalind_tree.txt", "r") as f:
    n = int(f.readline())
    adjacency_list = [line.strip().split(" ") for line in f]


subtrees = [] 
nodes = set() 
for i, j in adjacency_list:
    if i in nodes or j in nodes:
        for st in subtrees:
            if i in st or j in st:
                subtrees[subtrees.index(st)].append(i)
                subtrees[subtrees.index(st)].append(j)
                nodes.add(i), nodes.add(j)
    else:
        subtrees.append([i,j])
        nodes.add(i), nodes.add(j)

l = len(subtrees)
for i in range(l):
    for j in range(l):
        if i==j:
           break
        if len(set(subtrees[i] + subtrees[j])) < len(subtrees[i]) + len(subtrees[j]):
            subtrees[i] = list(set(subtrees[i] + subtrees[j]))
            subtrees[j] = []
subtrees = [i for i in subtrees if i]


result = (n -len(nodes)) + len(subtrees) 
print(result)