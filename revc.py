dataset = "CGAGTCCTCAAAAAGTAGTGTCGTAGTGAAGGGCGGATCTGGTGCGTGCGGTCGTACACTTAAAGTTGTCTCATGCTGACCGTACAATCCGTAACTTCCACGTAAGCCGCGGCCGTGAACCACCATGAGGGCGCATTGTGCCGCGTAAACTGGGCGTAATTTCAGTTGGGGAGAGGTACGACGATCTCTGTATACGGTTTGTCCGCGGAAGGAAAGGCCTCTCTTGAGTGGGAGGCTTGATTTGCGATCAAGGGCGCTGCCCGGGTTGACCTGGTCCTCTGTAAGCATCTGACCATTGTTATCTACTTGATTTCTACGAGGGGGTAATATATTAGATTGCCAAGTCCCTAATCAAGGCAGACGATCTATAAAAGCTGAACCTGACCGGGCAGATGAACTACAGACCGCTACCCAGTACTAACTAGGATATACCAGACGACCCGAAGCGGTCTTACTAAAAACTCACATATATGTCCTTGTAGGAAGCATTTCTTTCATAAATGGGGTGTCAGACGAGTCTTTTATTCAATAAGCTATCAAACAAGATGATTCATCCCAAAGCGTTGGTCTTCAGAATTCATTTGGCAACGGCTGCCATGGTCCGAAGACGGTCTGGCCTGCTCCCGAAGCGACATGCGTGTCTAACGATTGCGCAGCATCCTAATAATAATGACAAGTCGAGGGGGTAAGGGTACCCTAACTTGAAAGTTCTAAATCACATTACACTGACCGTTCCCTACGCCAGGAGAAATTCCCATCGTTTTTGTTGTATGTCGCTGGTACTACGTTAAGACGATCTCATTGACGATGTTTGACCGACGGTTTTTTCCTGCCTCTATTGGAGGCGCCTTAACGCTTAGAAGCCGCGTCGTGCGGTCACTTCGTCAGGAGGC"

rev = dataset[::-1]
rev = rev.replace("A","X")
rev = rev.replace("T","A")
rev = rev.replace("X","T")

rev = rev.replace("C","X")
rev = rev.replace("G","C")
rev = rev.replace("X","G")
print(rev)