seq="ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA"
GTGTGT_Count=0
GTCTGT_Count=0
length_seq=len(seq)
for start in range(length_seq):
    if seq[start:start+6]=="GTGTGT":
        GTGTGT_Count=GTGTGT_Count+1
    elif seq[start:start+6]=="GTCTGT":
        GTCTGT_Count=GTCTGT_Count+1
print("The GTGTGT count is ",GTGTGT_Count)
print("The GTCTGT count is ",GTCTGT_Count)
