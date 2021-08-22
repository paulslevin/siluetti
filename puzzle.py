from rules import rule1


class Puzzle:
    def __init__(self, num_rows: int, num_cols: int) -> None:
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.grid = [["0" for _ in range(num_cols)] for _ in range(num_rows)]
        self.row_clues = [[] * num_rows]
        self.col_clues = [[] * num_cols]

    def __str__(self):
        return "\n".join(" ".join(row) for row in self.grid)

    def apply_rule1_to_row(self, i: int):
        clues = self.row_clues[i]
        row = self.grid[i]
        rule1(clues, row)

    def apply_rule1_to_col(self, i: int):
        clues = self.col_clues[i]
        col = [row[i] for row in self.grid]
        rule1(clues, col)
        j = 0
        while j < self.num_rows:
            self.grid[j][i] = col[j]
            j += 1

    def apply_rule1_to_rows(self):
        i = 0
        while i < self.num_rows:
            self.apply_rule1_to_row(i)
            i += 1

    def apply_rule1_to_cols(self):
        i = 0
        while i < self.num_cols:
            self.apply_rule1_to_col(i)
            i += 1
