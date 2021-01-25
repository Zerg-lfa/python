class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join([' '.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for l in range(len(other.matrix[i])):
                self.matrix[i][l] = self.matrix[i][l] + other.matrix[i][l]
        return self.matrix




a = Matrix([[30, 20], [30, 40], [50, 80]])
b = Matrix([[30, 20], [30, 40], [50, 80]])
print(a)
print(a + b)