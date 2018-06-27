import math
from data_sets import DataSets

# 確率
_x = [0, 0]
X = [_x, _x]

X[0][0] = 0.6
X[0][1] = X[1][0] = 0.1
X[1][1] = 0.2


def Sg(y: tuple, n1=3, n2=3, sigma=1.0):
    def calc_exp(x1, x2):
        x = (x1, x2)
        result = 0
        for i in range(2):
            for j in range(n[i]):
                result += (1 - 2 * y[i][j] + 2 * y[i][j] * x[i] - x[i] ** 2) / sigma
        return result

    def hG(y, x_probability=X[1][1]):
        result = 0
        for i in range(0, 1):
            for j in range(0, 1):
                result += X[i][j] * math.exp(calc_exp(i, j))
        return result / x_probability

    n = [n1, n2]
    return 1 / hG(y)


if __name__ == '__main__':
    data = DataSets(3, 3)
    data.create_data_sets(1)
    sg = Sg(data.sets[0]['y'], 3, 3, 1.0)
