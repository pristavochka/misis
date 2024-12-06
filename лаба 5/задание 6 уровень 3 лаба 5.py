#Поменять местами столбец, содержащий максимальный элемент на главной диагонали заданной квадратной матрицы, со столб- цом, содержащим максимальный элемент в первой строке матрицы. Для замены столбцов использовать метод. Для поиска соответствующих максимальных элементов использовать делегат.
class Matrix:
    def __init__(self, data):
        self.data = data
    def diagonal_finder(self):
        n = len(self.data)
        mv = self.data[0][0]
        mi = 0
        for i in range(n):
            if self.data[i][i] > mv:
                mv = self.data[i][i]
                mi = i
        return mi
    def row_finder(self):
        mv = self.data[0][0]
        mi = 0
        for j in range(len(self.data[0])):
            if self.data[0][j] > mv:
                mv = self.data[0][j]
                mi = j
        return mi
    def move(self, col1, col2):
        for i in range(len(self.data)):
            self.data[i][col1], self.data[i][col2] = self.data[i][col2], self.data[i][col1]
    def print_matrix(self):
        for row in self.data:
            print(' '.join(map(str, row)))
matrix_data = [
[3, 2, 1],
[5, 6, 7],
[9, 0, 2],
]
matrix = Matrix(matrix_data)
matrix.print_matrix()
id = matrix.diagonal_finder()
ir = matrix.row_finder()
matrix.move(id, ir)
matrix.print_matrix()