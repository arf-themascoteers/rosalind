from enum import Enum
class Allele(Enum):
    DOMINANT = 1,
    RECESSIVE = 2,
    HET = 3


def mate(x,y):
    if x == Allele.DOMINANT and y == Allele.DOMINANT:
        return [Allele.DOMINANT]*4
    if x == Allele.RECESSIVE and y == Allele.RECESSIVE:
        return [Allele.RECESSIVE]*4
    if x == Allele.HET and y == Allele.HET:
        return [Allele.DOMINANT, Allele.HET, Allele.HET, Allele.RECESSIVE]
    if x == Allele.HET:
        return [Allele.HET, Allele.HET, y, y]
    if y == Allele.HET:
        return [Allele.HET, Allele.HET, x, x]
    else:#DOMINANT AND RECISSIVE
        return [Allele.HET]*4


def get_pairs(organisms):
    if len(organisms) < 2:
        return list()
    first = organisms[0]
    pairs = [(first, organisms[second_index]) for second_index in range(1, len(organisms))]
    other_pairs = get_pairs(organisms[1:])
    pairs.extend(other_pairs)
    return pairs

def f(k,m,n):
    organisms = list()
    for i in range(k):
        organisms.append(Allele.DOMINANT)
    for i in range(m):
        organisms.append(Allele.HET)
    for i in range(n):
        organisms.append(Allele.RECESSIVE)
    pairs = get_pairs(organisms)
    children_list = [mate(*p) for p in pairs]
    children = [child for sublist in children_list for child in sublist]
    count_children = len(children)
    count_dominant_presence = 0
    for child in children:
        if child is not Allele.RECESSIVE:
            count_dominant_presence += 1

    return count_dominant_presence/count_children

k = 30
m = 21
n = 18
print(f(k,m,n))
