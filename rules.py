def slice_length(clues, i, p, m):
    return clues[i] + sum(clues) + p - m - 1


def rule1(clues, row):
    m = len(row)
    p = len(clues)
    upper_bound = -2
    complete = sum(clues) + p - 1 == m
    for i, clue in enumerate(clues):
        upper_bound += clue + 1
        l = slice_length(clues, i, p, m)
        if l > 0:
            j = upper_bound - l + 1
            while j <= upper_bound:
                row[j] = "1"
                j += 1
            if complete and j < m:
                row[j] = "X"
