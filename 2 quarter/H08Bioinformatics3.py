
file = open("sequences.fasta")
lines = file.readlines()
seq1 = lines[0]
seq2 = lines[1]

# LOCAL ALIGNMENT__________________________________________________________________________________________________________
pathways = []

# Stores the resulting alignments
alignments = []


def waterman(seq1, seq2):
    """
    Perform local alignment (Smith–Waterman algorithm) between two sequences.

    Parameters
    ----------
    seq1 : str
        First sequence
    seq2 : str
        Second sequence

    This function:
    - Initializes the scoring matrix
    - Computes local alignment scores
    - Finds the maximum score in the matrix
    - Performs traceback from all maximum-score cells
    """
    global sequence_1, sequence_2
    global matrix, matrix_row, matrix_column

    sequence_1 = seq1
    sequence_2 = seq2

    # Matrix dimensions (+1 for initial zero row/column)
    matrix_row = len(sequence_1) + 1
    matrix_column = len(sequence_2) + 1

    # Each cell stores: [score, list_of_directions]
    matrix = [[[[None] for i in range(2)]
               for i in range(matrix_column)]
               for i in range(matrix_row)]

    # Fill scoring matrix
    i, j = scoring(1, -1, -1)

    # Find the maximum score in the matrix
    max_score = 0
    for k in range(1, matrix_row):
        for m in range(1, matrix_column):
            max_score = matrix[k][m][0] if matrix[k][m][0] > max_score else max_score

    # Start traceback from every cell with the maximum score
    while (i >= 0) and (j >= 0):
        if matrix[i][j][0] == max_score:
            tot_aln = find_pathways(i, j)
            print('Total Number of Alignments - Waterman:', tot_aln)
            traceback(i, j)
        i -= 1
        j -= 1


def scoring(match, mismatch, gap):
    """
    Fill the scoring matrix for local alignment.

    Parameters
    ----------
    match : int
        Score for a match
    mismatch : int
        Penalty for a mismatch
    gap : int
        Gap penalty

    Returns
    -------
    (i, j) : tuple
        Indices of the last filled cell
    """
    global match_score, mismatch_score, gap_penalty

    match_score = match
    mismatch_score = mismatch
    gap_penalty = gap

    # Initialize first row and column with zeros (local alignment)
    for i in range(matrix_row):
        matrix[i][0] = [0, []]
    for j in range(matrix_column):
        matrix[0][j] = [0, []]

    # Fill the matrix
    for i in range(1, matrix_row):
        for j in range(1, matrix_column):
            score = match_score if sequence_1[i - 1] == sequence_2[j - 1] else mismatch_score

            # Possible moves
            left_val = matrix[i][j - 1][0] + gap_penalty
            diag_val = matrix[i - 1][j - 1][0] + score
            top_val = matrix[i - 1][j][0] + gap_penalty

            values = [left_val, diag_val, top_val]
            max_val = max(values)

            # Local alignment rule: no negative scores
            if max_val < 0:
                max_val = 0

            # Store score and all directions that lead to max score
            # Directions: 1 = left, 2 = diagonal, 3 = top
            matrix[i][j] = [max_val,
                            [idx + 1 for idx, v in enumerate(values) if v == max_val]]

    return i, j


def find_pathways(ii, jj, path=''):
    """
    Recursively find all optimal traceback paths.

    Parameters
    ----------
    ii, jj : int
        Starting cell indices
    path : str
        Encoded traceback path (sequence of directions)

    Returns
    -------
    int
        Number of pathways found
    """
    global pathways
    i, j = ii, jj

    # Stop traceback if score is zero (local alignment)
    if (i == 0 and j == 0) or matrix[i][j][0] == 0:
        pathways.append(path)
        return 2

    dir_n = len(matrix[i][j][1])  # Number of possible directions

    # If only one direction exists, follow it
    while dir_n <= 1:
        num_dir = matrix[i][j][1][0] if (i != 0 and j != 0) else \
                  (1 if i == 0 else (3 if j == 0 else 0))

        path += str(num_dir)

        if num_dir == 1:      # Left
            j -= 1
        elif num_dir == 2:    # Diagonal
            i -= 1
            j -= 1
        elif num_dir == 3:    # Top
            i -= 1

        dir_n = len(matrix[i][j][1])

        if (i == 0 and j == 0) or matrix[i][j][0] == 0:
            pathways.append(path)
            return 1

    # If multiple directions exist, branch recursively
    for k in range(dir_n):
        num_dir = matrix[i][j][1][k]
        temp_path = path + str(num_dir)

        if num_dir == 1:
            find_pathways(i, j - 1, temp_path)
        elif num_dir == 2:
            find_pathways(i - 1, j - 1, temp_path)
        elif num_dir == 3:
            find_pathways(i - 1, j, temp_path)

    return len(pathways)


def traceback(ii, jj):
    """
    Construct aligned sequences from traceback paths.

    Parameters
    ----------
    ii, jj : int
        Starting position for traceback
    """
    global alignments
    count = 0

    for elem in pathways:
        i, j = ii - 1, jj - 1
        left_aln, top_aln = '', ''
        aln_info = []
        step = 0

        for direction in elem:
            step += 1
            score = matrix[i + 1][j + 1][0]
            aln_info.append([step, score, direction])

            if direction == '2':      # Diagonal
                left_aln += sequence_1[i]
                top_aln += sequence_2[j]
                i -= 1
                j -= 1
            elif direction == '1':    # Left
                left_aln += '-'
                top_aln += sequence_2[j]
                j -= 1
            elif direction == '3':    # Top
                left_aln += sequence_1[i]
                top_aln += '-'
                i -= 1

        count += 1
        alignments.append([top_aln[::-1], left_aln[::-1], elem, aln_info, count])

    print_alignments(alignments)


def print_alignments(alignments):
    """
    Print all computed alignments.
    """
    for elem in alignments:
        print(elem[0])
        print(elem[1])
        print()


# Run local alignment

waterman('ACATAG','AATG')


# GLOBAL ALIGNMENT__________________________________________________________________________________________________________

pathways = []
alignments = []


def needle(seq1, seq2):
    """
    Perform global alignment (Needleman–Wunsch algorithm).

    Parameters
    ----------
    seq1 : str
        First sequence
    seq2 : str
        Second sequence
    """
    global sequence_1, sequence_2
    global matrix, matrix_row, matrix_column

    sequence_1 = seq1
    sequence_2 = seq2

    matrix_row = len(sequence_1) + 1
    matrix_column = len(sequence_2) + 1

    matrix = [[[[None] for i in range(2)]
               for i in range(matrix_column)]
               for i in range(matrix_row)]

    i, j = scoring(1, -1, -1)

    tot_aln = find_pathways(i, j)
    print('Total Number of Alignments - Needle:', tot_aln)
    traceback(i, j)


# Run global alignment
needle(seq2, seq2)