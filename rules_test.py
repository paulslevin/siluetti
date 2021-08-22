import unittest
from rules import rule1


class TestRule1(unittest.TestCase):
    def test_rule1(self):
        clues = [4, 3, 2]
        row = ["0"] * 12
        rule1(clues, row)
        self.assertEqual(
            ["0", "1", "1", "1", "0", "0", "1", "1", "0", "0", "1", "0"],
            row,
        )

    def test_rule1_palkkio_col_6(self):
        clues = [1, 1, 1, 4, 1]
        row = ["0"] * 15
        rule1(clues, row)
        self.assertEqual(
            [
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "0",
            ],
            row,
        )

        row = [
            "0",
            "1",
            "0",
            "0",
            "0",
            "0",
            "1",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "0",
            "1",
        ]
        rule1(clues, row)
        self.assertEqual(
            [
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
                "0",
                "0",
                "1",
                "0",
                "0",
                "0",
                "0",
                "1",
            ],
            row,
        )

    def test_rule1_complete_clues(self):
        clues = [4, 3, 2]
        row = ["0"] * 11
        rule1(clues, row)
        self.assertEqual(
            ["1", "1", "1", "1", "X", "1", "1", "1", "X", "1", "1"],
            row,
        )


if __name__ == "__main__":
    unittest.main()
