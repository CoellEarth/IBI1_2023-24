import re
fasta_file_path = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
genes_dict = {}
with open(fasta_file_path, 'r') as fasta_file:
    for line in fasta_file:
        if line.startswith('>'):
            gene_name = str(re.findall(r'gene:.+?\s',line))
            genes_dict[gene_name] = ""
        else:
            genes_dict[gene_name] += line.strip()
genes = input('Please enter your sequences: ')
if genes == 'GTGTGT':
    with open('GTGTGT_duplicate_genes.fa','w') as f1:  
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_sequence.count('GTGTGT')
            if count !=0:
                f1.write(f"The repeat sequence '{'GTGTGT'}' appears {count} times in the gene '{gene_name}'."+'\n'+ gene_sequence + '\n')
if genes == 'GTCTGT':
    with open('GTCTGT_duplicate_genes.fa','w') as f2:
        for gene_name, gene_sequence in genes_dict.items():
            count = gene_sequence.count('GTCTGT')
            if count !=0:
                f2.write(f"The repeat sequence '{'GTCTGT'}' appears {count} times in the gene '{gene_name}'."+'\n'+ gene_sequence + '\n')

