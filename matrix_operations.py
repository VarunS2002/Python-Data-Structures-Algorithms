from typing import Optional, Union

matrix = list[list[float]]
dimensions = tuple[int, int]


class MatrixOperations:
    class IncompatibleDimensionsError(Exception):
        def __str__(self) -> str:
            return "Matrices are not compatible.\n" \
                   "No. of Columns in Matrix 1 have to be the same as No. of Rows in Matrix 2."

    @staticmethod
    def __get_dimensions(matrix_1: matrix, matrix_2: Optional[matrix] = None) -> \
            Union[tuple[dimensions, bool], tuple[dimensions, dimensions, bool, bool]]:
        rows_1: int = len(matrix_1)
        cols_1: int = len(matrix_1[0])
        dim_1: dimensions = (rows_1, cols_1)
        if matrix_2 is not None:
            rows_2: int = len(matrix_2)
            cols_2: int = len(matrix_2[0])
            dim_2: dimensions = (rows_2, cols_2)
            same_dim: bool = dim_1 == dim_2
            compatible_dim: bool = cols_1 == rows_2
            return dim_1, dim_2, same_dim, compatible_dim
        else:
            square: bool = rows_1 == cols_1
            return dim_1, square

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
        same_dim: bool
        compatible_dim: bool
        dim_1, dim_2, same_dim, compatible_dim = MatrixOperations.__get_dimensions(matrix_1, matrix_2)
        if not same_dim:
            raise MatrixOperations.IncompatibleDimensionsError
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
        same_dim: bool
        compatible_dim: bool
        dim_1, dim_2, same_dim, compatible_dim = MatrixOperations.__get_dimensions(matrix_1, matrix_2)
        if not same_dim:
            raise MatrixOperations.IncompatibleDimensionsError
        difference_m: matrix = [[0 for cols in range(dim_1[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_1[1]):
                difference_m[i][j] = matrix_1[i][j] - matrix_2[i][j]
        return difference_m

    # noinspection PyUnusedLocal
    @staticmethod
    def multiplication(matrix_1: matrix, matrix_2: matrix) -> matrix:
        dim_1: dimensions
        dim_2: dimensions
        same_dim: bool
        compatible_dim: bool
        dim_1, dim_2, same_dim, compatible_dim = MatrixOperations.__get_dimensions(matrix_1, matrix_2)
        if not compatible_dim:
            raise MatrixOperations.IncompatibleDimensionsError
        product_m: matrix = [[0 for cols in range(dim_2[1])] for rows in range(dim_1[0])]
        for i in range(0, dim_1[0]):
            for j in range(0, dim_2[1]):
                for k in range(0, dim_2[0]):
                    product_m[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return product_m

    # noinspection PyUnusedLocal
    @staticmethod
    def transpose(matrix_1: matrix) -> matrix:
        dim: dimensions
        square: bool
        dim, square = MatrixOperations.__get_dimensions(matrix_1)
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
    print('Identity Matrix:')
    MatrixOperations.display(MatrixOperations.identity(3))
