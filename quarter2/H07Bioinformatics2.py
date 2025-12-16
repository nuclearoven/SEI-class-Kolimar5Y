
def readFASTA(filename):
    """opens fasta file and loops through each line
    if the line starts with '>' it prints "identifier line:" and ignores it
    else it adds it into the curr_seq list
    returns the joined curr_seq list"""
    file = open(filename)
    curr_seq = []
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            print("Found an identifier line:", line)
        else:
            curr_seq.append(line)
    return ''.join(curr_seq)

def readDNA(filename):
    """opens fasta file and loops through each line
    if the line starts with '>' it prints "identifier line:" and ignores it
    else it adds it into the curr_seq list
    returns the joined curr_seq list"""
    file = open(filename)
    curr_seq = []
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            print("Found an identifier line:", line)
        else:
            curr_seq.append(line)
    return ''.join(curr_seq)

def readRNA(filename):
    """opens fasta file and loops through each line
    if the line starts with '>' it prints "identifier line:" and ignores it
    else it adds it into the curr_seq list
    returns the joined curr_seq list"""
    file = open(filename)
    curr_seq = []
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            print("identifier line:", line)
        else:
            curr_seq.append(line)
    return ''.join(curr_seq)
def readProtein(filename):
    """opens fasta file and loops through each line
    if the line starts with '>' it prints "identifier line:" and ignores it
    else it adds it into the curr_seq list
    returns the joined curr_seq list"""
    file = open(filename)
    curr_seq = []
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            print("identifier line:", line)
        else:
            curr_seq.append(line)
    return ''.join(curr_seq)

def uniqueCharacters(sequence):
    """loops through all letters of the sequence
     Checks if a character is in the list u_ch
     If the character is not already in the list it adds it"""
    s = sequence
    u_ch = []
    for char in s:
        # If the character is not already in the list, add it
        if char not in u_ch:
            u_ch.append(char)

    # Calculate the number of unique characters
    u_c = len(u_ch)
    print(f"Number of unique characters: {u_c}")
    return u_ch


print(uniqueCharacters(readDNA('Human_X_Chromosome_FMR_Region_NCBI.fasta')))
print(uniqueCharacters(readRNA('Human_X_Chromosome_FMR_Region_NCBI.fasta')))
print(uniqueCharacters(readProtein('Human_FMR1_Protein_UniProt.fasta')))
sequence = uniqueCharacters(readFASTA('Human_FMR1_Protein_UniProt.fasta'))
#checks if the sequence is a nucleotide, if yes it checks which one
if len(sequence) ==4:
    if sequence == ["C","T","A","G"]:
        print("Fasta contains DNA sequences")
    if sequence == ["C","U","A","G"]:
        print("Fasta contains RNA sequences")
else:
    print("Fasta contains Protein sequences")