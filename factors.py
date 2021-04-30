from typing import Optional


class Factors:
    @staticmethod
    def factors_iteration(number: int, use_while: bool = False) -> list[int]:
        factors: list[int] = []
        negative_factors: bool = False
        if number == 0:
            raise ArithmeticError("Factors of zero don't exist.")
        elif not isinstance(number, int):
            raise ArithmeticError("Factors of non-integers is not supported.")
        elif number < 0:
            negative_factors = True
        if use_while:
            i: int = 1
            while i < abs(number) + 1:
                if abs(number) % i == 0:
                    factors.append(i)
                    if negative_factors:
                        factors.append(-1 * i)
                i += 1
        else:
            for i in range(1, abs(number) + 1):
                if abs(number) % i == 0:
                    factors.append(i)
                    if negative_factors:
                        factors.append(-1 * i)
        return factors

    @staticmethod
    def factors_recursion(number: int) -> list[int]:
        return Factors.__factors_recursion_implementation(number)

    @staticmethod
    def __factors_recursion_implementation(number: int, next_factor: Optional[int] = None,
                                           factors: Optional[list[int]] = None,
                                           negative_factors: bool = False) -> list[int]:
        if next_factor is None and factors is None:
            factors = []
            next_factor = abs(number)
            if number == 0:
                raise ArithmeticError("Factors of zero don't exist.")
            elif not isinstance(number, int):
                raise ArithmeticError("Factors of non-integers is not supported.")
            elif number < 0:
                negative_factors = True
        if next_factor == 0:
            return list(reversed(factors))
        elif abs(number) % next_factor == 0:
            if negative_factors:
                factors.append(-1 * next_factor)
            factors.append(next_factor)
        return Factors.__factors_recursion_implementation(number, next_factor - 1, factors, negative_factors)


if __name__ == '__main__':
    input_number = int(input("Enter a non-zero integer: "))
    print("Using iteration (for):", Factors.factors_iteration(input_number))
    print("Using iteration (while):", Factors.factors_iteration(input_number, use_while=True))
    print("Using recursion:", Factors.factors_recursion(input_number))
