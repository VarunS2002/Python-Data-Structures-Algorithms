from typing import Optional, Union

matrix = list[list[float]]
dimensions = tuple[int, int]


class MatrixOperations:
    class IncompatibleDimensionsError(Exception):
        def __init__(self, message: Optional[str] = None) -> None:
            self.message = message if message else "Incompatible dimensions"

        def __str__(self) -> str:
            return self.message

    @staticmethod
    def get_dimensions(matrix_1: matrix, matrix_2: Optional[matrix] = None) -> \
            Union[dimensions, tuple[dimensions, dimensions]]:
        rows_1: int = len(matrix_1)
        cols_1: int = len(matrix_1[0])
        dim_1: dimensions = (rows_1, cols_1)
        if matrix_2 is not None:
            rows_2: int = len(matrix_2)
            cols_2: int = len(matrix_2[0])
            dim_2: dimensions = (rows_2, cols_2)
            return dim_1, dim_2
        else:
            return dim_1

    @staticmethod
    def is_square(matrix_1: matrix) -> bool:
        dim: dimensions = MatrixOperations.get_dimensions(matrix_1)
        return dim[0] == dim[1]

    @staticmethod
    def have_same_dimensions(matrix_1: matrix, matrix_2: matrix) -> bool:
        dim_1: dimensions
        dim_2: dimensions
        dim_1, dim_2 = MatrixOperations.get_dimensions(matrix_1, matrix_2)
        return dim_1 == dim_2

    @staticmethod
    def have_multipliable_dimensions(matrix_1: matrix, matrix_2: matrix) -> bool:
        dim_1: dimensions
        dim_2: dimensions
        dim_1, dim_2 = MatrixOperations.get_dimensions(matrix_1, matrix_2)
        return dim_1[1] == dim_2[0]

    # noinspection PyUnusedLocal
    @staticmethod
    def identity(dimension: int) -> matrix:
        identity_m: matrix = [[0 for cols in range(dimension)] for rows in range(dimension)]
        for i in range(0, dimension):
            identity_m[i][i] = 1
        return identity_m

    # noinspection PyUnusedLocal
    @staticmethod
    def addition(matrix_1: matrix, matrix_2: matrix) -> matrix:
        dim_1: dimensions
        dim_2: dimensions
        dim_1, dim_2 = MatrixOperations.get_dimensions(matrix_1, matrix_2)
        have_same_dimensions: bool = MatrixOperations.have_same_dimensions(matrix_1, matrix_2)
        if not have_same_dimensions:
            raise MatrixOperations.IncompatibleDimensionsError("Matrices are not compatible.\n"
                                                               "No. of Rows & Columns in Matrix 1 have to be the same "
                                                               "as No. of Rows & Columns in Matrix 2.")
        sum_m: matrix = [[0 for cols in range(dim_1[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_1[1]):
                sum_m[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return sum_m

    # noinspection PyUnusedLocal
    @staticmethod
    def subtraction(matrix_1: matrix, matrix_2: matrix) -> matrix:
        dim_1: dimensions
        dim_2: dimensions
        dim_1, dim_2 = MatrixOperations.get_dimensions(matrix_1, matrix_2)
        have_same_dimensions: bool = MatrixOperations.have_same_dimensions(matrix_1, matrix_2)
        if not have_same_dimensions:
            raise MatrixOperations.IncompatibleDimensionsError("Matrices are not compatible.\n"
                                                               "No. of Rows & Columns in Matrix 1 have to be the same "
                                                               "as No. of Rows & Columns in Matrix 2.")
        difference_m: matrix = [[0 for cols in range(dim_1[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_1[1]):
                difference_m[i][j] = matrix_1[i][j] - matrix_2[i][j]
        return difference_m

    # noinspection PyUnusedLocal
    @staticmethod
    def scalar_multiplication(matrix_1: matrix, scalar: float) -> matrix:
        dim: dimensions = MatrixOperations.get_dimensions(matrix_1)
        product_m: matrix = [[0 for cols in range(dim[1])] for rows in range(dim[0])]
        for i in range(0, dim[0]):
            for j in range(0, dim[1]):
                product_m[i][j] = matrix_1[i][j] * scalar
        return product_m

    # noinspection PyUnusedLocal
    @staticmethod
    def multiplication(matrix_1: matrix, matrix_2: matrix) -> matrix:
        dim_1: dimensions
        dim_2: dimensions
        dim_1, dim_2 = MatrixOperations.get_dimensions(matrix_1, matrix_2)
        have_multipliable_dimensions: bool = MatrixOperations.have_multipliable_dimensions(matrix_1, matrix_2)
        if not have_multipliable_dimensions:
            raise MatrixOperations.IncompatibleDimensionsError("Matrices are not compatible.\n"
                                                               "No. of Columns in Matrix 1 have to be the same as No. "
                                                               "of Rows in Matrix 2.")
        product_m: matrix = [[0 for cols in range(dim_2[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_2[1]):
                for k in range(0, dim_2[0]):
                    product_m[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return product_m

    # noinspection PyUnusedLocal
    @staticmethod
    def transpose(matrix_1: matrix) -> matrix:
        dim: dimensions = MatrixOperations.get_dimensions(matrix_1)
        transpose_m: matrix = [[0 for cols in range(dim[0])] for rows in range(dim[1])]
        for i in range(0, dim[0]):
            for j in range(0, dim[1]):
                transpose_m[j][i] = matrix_1[i][j]
        return transpose_m

    @staticmethod
    def display(matrix_1: matrix) -> None:
        for row in matrix_1:
            print(row)


if __name__ == '__main__':
    m_1 = [[10, 20, 30], [40, 5, 6], [7, 8, 9]]
    m_2 = [[10, 20, 30], [40, 5, 6], [7, 8, 9]]
    m_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m_4 = [[1, 2], [4, 5], [7, 8]]
    scalar_value = 0.5

    addition = MatrixOperations.addition(m_1, m_2)
    difference = MatrixOperations.subtraction(m_1, m_2)
    transpose = MatrixOperations.transpose(m_3)
    product = MatrixOperations.multiplication(m_3, m_4)
    print('Matrix 1:')
    MatrixOperations.display(m_1)
    print('Matrix 2:')
    MatrixOperations.display(m_2)
    print('Matrix 3:')
    MatrixOperations.display(m_3)
    print('Matrix 4:')
    MatrixOperations.display(m_4)
    print('Transpose of Matrix 3:')
    MatrixOperations.display(transpose)
    print('Addition of Matrix 1 & 2:')
    MatrixOperations.display(addition)
    print('Subtraction of Matrix 1 & 2:')
    MatrixOperations.display(difference)
    print('Multiplication of Matrix 3 & 4:')
    MatrixOperations.display(product)
    print(f'Scalar Multiplication of Matrix 1 by {scalar_value}:')
    MatrixOperations.display(MatrixOperations.scalar_multiplication(m_1, scalar_value))
    print('Identity Matrix:')
    MatrixOperations.display(MatrixOperations.identity(3))
