dataset = """>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC"""

nodes = []
labels = []
lines = ""

for line in dataset.splitlines():
    if line.startswith(">"):
        labels.append(line[1:])
        if lines != "":
            nodes.append(lines)
            lines = ""
    else:
        lines = lines + line
nodes.append(lines)

edges = []


def prefix(s, k):
    return s[0:k]


def postfix(s, k):
    return s[-k:]


for i in range(len(nodes)):
    edges.append([])

str_len = len(nodes)
pattern_len = str_len //2
if str_len % 2 == 1:
    pattern_len = pattern_len + 1
pattern_len=4
for i in range(len(nodes)):
    for j in range(0, len(nodes)):
        if i != j and postfix(nodes[i], pattern_len) == prefix(nodes[j], pattern_len):
            edges[i].append(j)

for i in range(len(edges)):
    for j in edges[i]:
        print(f"{i}-", end="")
        print(nodes[i], end=" ")
        print(f"{j}-", end="")
        print(nodes[j])
