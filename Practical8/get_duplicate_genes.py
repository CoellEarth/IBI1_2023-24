input_file_path = r"E:/IBI1_2023-24/Practical8/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file_path = r"E:/IBI1_2023-24/Practical8/duplicate_genes.fa"

with open(input_file_path, "r") as input_file, open(output_file_path, "w") as output_file:
    #set the initial values
    write_mode = False
    current_gene_name = ""
    current_gene_sequence = ""
    
    #read every line in the input file
    for line in input_file:
        
        #remove the \n at the end of every line
        line = line.strip() 
        if line.startswith(">"): 
            if write_mode:  
                output_file.write(">" + current_gene_name + "\n")
                output_file.write(current_gene_sequence + "\n")
            write_mode = False  
            
            #check if there is 'duplication' in the description
            if "duplication" in line:  
                write_mode = True
                #extract the names of the genes
                current_gene_name = line.split()[0][1:]  
                current_gene_sequence = ""  
        elif write_mode:  
            current_gene_sequence += line + "\n" 

    if write_mode:
        output_file.write(">" + current_gene_name + "\n")
        output_file.write(current_gene_sequence)
