import math
from data_sets import DataSets

# 確率
_x = [0, 0]
X = [_x, _x]

X[0][0] = 0.6
X[0][1] = X[1][0] = 0.1
X[1][1] = 0.2


def Sg(y: tuple, n1=3, n2=3, sigma=1.0, x_probability=X[1][1]):
    def calc_exp(x1, x2):
        x = (x1, x2)
        result = 0
        for i in range(2):
            for j in range(n[i]):
                result += (1 - 2 * y[i][j] + 2 * y[i][j] * x[i] - x[i] ** 2) / (2 * sigma ** 2)
        return math.exp(result)

    def hG():
        result = 0
        for i in range(2):
            for j in range(2):
                result += X[i][j] * calc_exp(i, j)
        return result / x_probability

    n = [n1, n2]
    return 1 / hG()


def St(y: tuple, n1=3, n2=3, sigma=1.0, x_probability=X[1][1]):
    def calc_exp():
        result = 0
        for i in range(2):
            for j in range(n[i]):
                result += (1 - 2 * y[i][j]) / (2 * (sigma ** 2))
        return math.exp(result)

    def hT():
        return 1 + (X[0][0] * calc_exp()) / X[1][1]

    n = [n1, n2]
    return 1 / hT()


if __name__ == '__main__':
    data = DataSets(3, 3)
    data.create_data_sets(1)
    sg = Sg(data.sets[0]['y'], 3, 3, 1.0)
