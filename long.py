from Bio import SeqIO
import io

def find_overlaps(reads_list, superstring=''):
    if len(reads_list) == 0:
        return superstring

    elif len(superstring) == 0:
        superstring = reads_list.pop(0)
        return find_overlaps(reads_list, superstring)

    else:

        for current_read_index in range(len(reads_list)):
            current_read = reads_list[current_read_index]
            current_read_length = len(current_read)

            for current_read_character_index in range(current_read_length // 2):
                overlap_length = current_read_length - current_read_character_index

                if superstring.startswith(current_read[current_read_character_index:]):
                    reads_list.pop(current_read_index)
                    return find_overlaps(reads_list, current_read[:current_read_character_index] + superstring)

                if superstring.endswith(current_read[:overlap_length]):
                    reads_list.pop(current_read_index)
                    return find_overlaps(reads_list, superstring + current_read[overlap_length:])


if __name__ == "__main__":

    small_dataset = """>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC"""
    handle = io.StringIO(small_dataset)

    reads = []
    for record in SeqIO.parse(handle, 'fasta'):
        reads.append(str(record.seq))
    handle.close()
    ov = find_overlaps(reads)
    print(ov)
