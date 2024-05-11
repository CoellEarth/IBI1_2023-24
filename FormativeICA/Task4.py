#1 Create a table which stores the correspondence between codons and amino acids
#2 Define a function called mRNA_polypeptide_convertor
#3 Create a string to store the corresponding amino acid and put all aa togrther 
#4 what start and stop codon(s) are 
#5 Find where the start codon is in the entire mRNA sequence, read 3 by 3 after it
#6 Make the reading stop if encountering stop codon
user_input = input("Please enter your mRNA sequence here: ")
correspondence_table = {'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',  #1
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
def mRNA_polypeptide_convertor(user_input): #2
    peptide_sequence = "" #3
    start_codon = "AUG" #4
    stop_codons = ["UAA", "UAG", "UGA"]
    start_index = user_input.find(start_codon) #5
    for i in range(start_index, len(user_input), 3):
        codon = user_input[i:i + 3]
        if codon in stop_codons: #6
            break
        else: #3
            amino_acid = correspondence_table.get(codon)
            peptide_sequence += amino_acid
    return peptide_sequence
print(mRNA_polypeptide_convertor(user_input))
