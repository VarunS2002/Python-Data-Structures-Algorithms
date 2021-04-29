from typing import Callable, Optional

from factorial import Factorial


class PermutationsCombinations:
    @staticmethod
    def npr(n: int, r: int) -> int:
        if not isinstance(n, int) or not isinstance(r, int):
            raise ArithmeticError("Cannot calculate nPr for non-integers.")
        elif not n >= r >= 0:
            raise ArithmeticError("Please enter n ≥ r ≥ 0.")
        factorial: Callable[[int, Optional[bool]], int] = Factorial.factorial_iteration
        return factorial(n) // factorial(n - r)

    @staticmethod
    def permutations(n: int, r: int) -> int:
        return PermutationsCombinations.npr(n, r)

    @staticmethod
    def ncr(n: int, r: int) -> int:
        if not isinstance(n, int) or not isinstance(r, int):
            raise ArithmeticError("Cannot calculate nCr for non-integers.")
        elif not n >= r >= 0:
            raise ArithmeticError("Please enter n ≥ r ≥ 0.")
        factorial: Callable[[int, Optional[bool]], int] = Factorial.factorial_iteration
        return factorial(n) // (factorial(r) * factorial(n - r))

    @staticmethod
    def combinations(n: int, r: int) -> int:
        return PermutationsCombinations.ncr(n, r)


if __name__ == '__main__':
    input_n = int(input("Enter n: "))
    input_r = int(input("Enter r: "))
    print("Permutations:", PermutationsCombinations.permutations(n=input_n, r=input_r))
    print("Combinations:", PermutationsCombinations.combinations(n=input_n, r=input_r))
