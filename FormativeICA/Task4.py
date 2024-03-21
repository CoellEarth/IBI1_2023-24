user_input = input("Please enter your mRNA sequence here:")
take_in_mRNA = str(user_input)

def task_4_function(take_in_mRNA):
    correspondence_table = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
                            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
                            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
                            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
                            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
                            'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
                            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
                            'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
                            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
                            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
                            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
                            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
                            'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
                            'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
                            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
                            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    peptide_sequence = ""
    start_codon = "AUG"
    stop_codon = ["UAA", "UAG", "UGA"]
    start_index = take_in_mRNA.find(start_codon)

    for i in range(start_index, len(take_in_mRNA), 3):
        codon = take_in_mRNA[i:i + 3]
        if codon in stop_codon:
            break
        else:
            amino_acid = correspondence_table.get(codon, "X")
            peptide_sequence = peptide_sequence + amino_acid

    print("(Note: If X appears in the polypeptide sequence, X means that there is no amino acid corresponding to this codon)")
    return peptide_sequence

print(task_4_function(take_in_mRNA))

