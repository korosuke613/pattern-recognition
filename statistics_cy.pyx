from data_sets import DataSets
from libc.math cimport exp, sqrt, M_PI

# 確率
_x = [0, 0]
X = [_x, _x]

X[0][0] = 0.6
X[0][1] = X[1][0] = 0.1
X[1][1] = 0.2
prx1 = [0.7, 0.3]
prx2 = [0.7, 0.3]


cdef class Sg:
    cdef tuple y
    cdef list n
    cdef int n1, n2
    cdef double sigma, x_probability

    def __init__(self, tuple y, int n1=3, int n2=3, double sigma=1.0, double x_probability=X[1][1]):
        self.y = y
        self.n1 = n1
        self.n2 = n2
        self.sigma = sigma
        self.x_probability = x_probability
        self.n = [self.n1, self.n2]

    cdef double calc_exp(self, int x1, int x2):
        cdef list x = [x1, x2]
        cdef double result = 0.0
        for i in range(2):
            for j in range(self.n[i]):
                result += (1 - 2 * self.y[i][j] + 2 * self.y[i][j] * x[i] - x[i] ** 2) / (2 * self.sigma ** 2)
        return exp(result)

    cdef double hG(self):
        cdef double result = 0.0
        for i in range(2):
            for j in range(2):
                result += X[i][j] * self.calc_exp(i, j)
        return result / self.x_probability

    cpdef double get(self):
        return 1 / self.hG()

cdef class St:
    cdef tuple y
    cdef list n
    cdef int n1, n2
    cdef double sigma, x_probability

    def __init__(self, y: tuple, n1=3, n2=3, sigma=1.0, x_probability=X[1][1]):
        self.y = y
        self.n1 = n1
        self.n2 = n2
        self.sigma = sigma
        self.x_probability = x_probability
        self.n = [self.n1, self.n2]

    cdef double calc_exp(self):
        cdef double result = 0.0
        for i in range(2):
            for j in range(self.n[i]):
                result += (1 - 2 * self.y[i][j]) / (2 * (self.sigma ** 2))
        return exp(result)

    cdef double hT(self):
        return 1 + (X[0][0] * self.calc_exp()) / X[1][1]

    cpdef double get(self):
        return 1 / self.hT()

cdef class Sp:
    cdef tuple y
    cdef list n
    cdef int n1, n2, first_row, second_row
    cdef double sigma, x_probability

    def __init__(self, tuple y, int n1=3, int n2=3, double sigma=1.0, isOneTwo=True):
        self.y = y
        self.n1 = n1
        self.n2 = n2
        self.sigma = sigma
        self.n = [self.n1, self.n2]
        if isOneTwo:
            row = (0, 1)
        else:
            row = (1, 0)
        self.first_row = row[0]
        self.second_row = row[1]

    def get_n(self):
        return self.n

    cpdef double get(self):
        return 1.0 / self.invert()
    cdef double invert(self):
        return self.pr1(self.n) * self.pr2(self.n)
    cpdef double pr1(self, list n_list):
        return 1 + ((X[0][0] + X[0][1]) / (X[1][0] + X[1][1]) * exp(self.inExp(n_list, self.first_row)))
    cdef double pr2(self, list n_list):
        return 1 + (X[1][0] / X[1][1] * exp(self.inExp(n_list, self.second_row)))
    cdef double inExp(self, list n_list, int i):
        cdef double w = 0.0
        cdef int j
        for j in range(n_list[i]):
            w += (1.0 - 2.0 * self.y[i][j]) / (2.0 * self.sigma * self.sigma)
        return w

if __name__ == '__main__':
    data = DataSets(3, 3)
    data.create_data_sets(1)
    sg = Sg(data.sets[0]['y'], 3, 3, 1.0)
