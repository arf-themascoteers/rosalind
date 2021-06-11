import math

dataset = "GGTTCACATGACCGTAGAAGTAGTGACTGTTATCTGTTCCCACGAGACAGTTAAGACAAAAGTCCTGAAGCAGGTCAAGTTGTCGCAACGAGGCGTGA"
number_line = "0.056 0.145 0.172 0.235 0.286 0.355 0.385 0.462 0.508 0.575 0.605 0.646 0.731 0.745 0.829 0.849 0.943"
gcc = [float(i) for i in number_line.split()]


outputs = []
prob = 0
for a_gcc in gcc:
    prob = 0
    chances = {
        'A' : (1-a_gcc)/2,
        'C' : a_gcc/2,
        'G' : a_gcc/2,
        'T' : (1-a_gcc)/2
    }
    for c in dataset:
        prob = prob + math.log10(chances[c])
    outputs.append(prob)

print(" ".join([str(i) for i in outputs]))