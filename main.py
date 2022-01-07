sequence1 = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'
sequence2 = 'GTCGTTCGGAATGCCGTTGCTCTGTAA'
pattern = 'GCCGGCC'

m = len(sequence1)
n = len(sequence2)
matrix = [[0] * (n + 1) for i in range(m + 1)]


def lcs_length():
    # Loop over each element of the matrix row by row.
    # (Row = i Column = j)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif sequence1[i - 1] == sequence2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[m][n]


def print_lcs():
    target = ''
    i, j = m, n
    # Starts at the bottom right of the matrix and goes up until
    # at the top left.
    while i > 0 and j > 0:
        # q = 1 when a matching letter is found.
        if sequence1[i-1] == sequence2[j-1]:
            q = 1
        else:
            q = 0
        if matrix[i][j] == matrix[i - 1][j - 1] + q:
            # Found a matching letter and add it to the
            # front of the string.
            if q == 1:
                target = sequence1[i - 1] + target
            i -= 1
            j -= 1
        elif matrix[i][j] == matrix[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return target


def naive_string_match(sequence):
    a = len(pattern)
    b = len(sequence)
    # Loop through the sequence until the length of sequence - pattern
    # because the pattern can't exist if there aren't enough letters left.
    for i in range(b-a+1):
        j = 0
        # Loops through the pattern.
        while j < a:
            # If the letter doesn't match break the while loop
            if sequence[i+j] != pattern[j]:
                break
            j += 1
            # A complete match is found and return the index the pattern
            # starts at inside the sequence.
            if j == a:
                return i
    # Return -1 if pattern isn't found.
    return -1


if __name__ == '__main__':
    length = lcs_length()
    prt = print_lcs()
    naive1 = naive_string_match(sequence1)
    naive2 = naive_string_match(sequence2)

    # Writing result files.
    f = open('results.txt', 'w')
    f.write(str(length) + '\n' + prt)
    f.close()

    f = open('bonusResults.txt', 'w')
    f.write(str(naive1) + '\n' + str(naive2))
    f.close()

    # Even though I'm writing all the results out to files I left the print
    # statements in because I started with them.
    print('The length of LCS is:', length)
    print('The LCS is:', prt)
    if naive1 != -1:
        print(f"Naive string match for sequence 1: '{pattern}' found"
              f" at index {naive1} through {naive1+len(pattern)}")
    else:
        print(f"Naive string match for sequence 1: {naive1}, "
              f"'{pattern}' not found in sequence")

    if naive2 != -1:
        print(f"Naive string match for sequence 1: '{pattern}' found"
              f" at index {naive2} through {naive2+len(pattern)}")
    else:
        print(f"Naive string match for sequence 2: {naive2}, "
              f"'{pattern}' not found in sequence")
