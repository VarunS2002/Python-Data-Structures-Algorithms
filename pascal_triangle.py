from permutations_combinations import PermutationsCombinations


class PascalTriangle:
    @staticmethod
    def pascal_triangle(rows: int) -> None:
        if not isinstance(rows, int):
            raise ArithmeticError("Number of rows in a Pascal's triangle cannot be non-integers.")
        elif rows < 0:
            raise ArithmeticError("Number of rows in a Pascal's triangle cannot be negative.")
        for n in range(rows):
            for r in range(rows - n + 1):
                print(end="  ")
            for r in range(n + 1):
                print(PermutationsCombinations.ncr(n, r), end='   ' if r != n else '')
            print()


if __name__ == '__main__':
    PascalTriangle.pascal_triangle(int(input("Enter the number of rows: ")))
