import re

input_file = r"C:\Users\32771\Desktop\IBI\practical\materials\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "duplicated_genes.fa"

with open(input_file, 'r') as f:
    content = f.read()


with open(output_file, 'w') as t:
    t.write(content)

with open(output_file, "a") as g:
    third_modified_content_part = content.split(">")
    duplicated_genes = []
    for part in third_modified_content_part:
        if "duplication" in part:
            start_index = part.find("]")
            gene_names = ">"+part.split(" ")[0]
            gene_sequence = part[start_index + 1:]
            g.write(gene_names + gene_sequence+"\n")









