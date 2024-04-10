import re

input_file = r"C:\Users\32771\Desktop\IBI\practical\materials\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "second_file.fasta"

with open(input_file, 'r') as f:
    content = f.read()


with open(output_file, 'w') as t:
    t.write(content)

with open(output_file, "+r") as g:
    modified_content = g.read()
    third_modified_content_part = modified_content.split(">")
    duplicated_genes = []
    for part in third_modified_content_part:
        if "duplication" in part:
            start_index = part.find("]")
            gene_names = ">"+part.split(" ")[0]
            gene_sequence = part[start_index + 1:]
            duplicated_genes.append(gene_names + "\n" + gene_sequence)

for gene_info in duplicated_genes:
    print(gene_info)

