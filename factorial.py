class Factorial:
    @staticmethod
    def factorial_iteration(number: int, use_while: bool = False) -> int:
        factorial: int = 1
        if number < 0:
            raise ArithmeticError("Factorial of a negative number doesn't exist.")
        elif not isinstance(number, int):
            raise ArithmeticError("Factorial of non-integers is not supported.")
        elif number == 0 or number == 1:
            return factorial
        else:
            if use_while:
                i: int = 1
                while i < number + 1:
                    factorial *= i
                    i += 1
            else:
                for i in range(1, number + 1):
                    factorial *= i
        return factorial

    @staticmethod
    def factorial_recursion(number: int) -> int:
        if number < 0:
            raise ArithmeticError("Factorial of a negative number doesn't exist.")
        elif not isinstance(number, int):
            raise ArithmeticError("Factorial of non-integers is not supported.")
        elif number == 0 or number == 1:
            return 1
        else:
            return number * Factorial.factorial_recursion(number - 1)


if __name__ == '__main__':
    input_number = int(input("Enter a positive integer: "))
    print("Using iteration (for):", Factorial.factorial_iteration(input_number))
    print("Using iteration (while):", Factorial.factorial_iteration(input_number, use_while=True))
    print("Using recursion:", Factorial.factorial_recursion(input_number))
