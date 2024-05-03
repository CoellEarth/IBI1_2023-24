#Interact with the user to get their input 
user_input = input("Please enter your mRNA sequence here: ")
#Create a table which stores the correspondence between codons and amino acids
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
#Define a function called mRNA_polypeptide_convertor
def mRNA_polypeptide_convertor(user_input):
    #Create a string to store the corresponding amino acid 
    peptide_sequence = ""
    #Give the information of what start and stop codon(s) are
    start_codon = "AUG"
    stop_codons = ["UAA", "UAG", "UGA"]
    #Find where the start codon is in the entire mRNA sequence
    start_index = user_input.find(start_codon)
    #From the start codon found, read the nucleotide three by three
    for i in range(start_index, len(user_input), 3):
        codon = user_input[i:i + 3]
        #Make the reading stop if encountering stop codon
        if codon in stop_codons:
            break
        #Construct correspondence and and the amino acid to the string
        else:
            amino_acid = correspondence_table.get(codon)
            peptide_sequence += amino_acid
    #return the result: peptide_sequence
    return peptide_sequence
#Print it out to make the user see the result
print(mRNA_polypeptide_convertor(user_input))
