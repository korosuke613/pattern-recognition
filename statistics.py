import math
from data_sets import DataSets

# 確率
_x = [0, 0]
X = [_x, _x]

X[0][0] = 0.6
X[0][1] = X[1][0] = 0.1
X[1][1] = 0.2
prx1 = [0.7, 0.3]
prx2 = [0.7, 0.3]


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


def Sp(y: tuple, n1=3, n2=3, sigma=1.0, x_probability=X[1][1]):
    def pyx(x, yi):
        result = 0
        for y in yi:
            result += math.exp(-((y - x) ** 2) / (2 * sigma ** 2)) / (2 * math.pi * sigma)
        return result

    def prxy(y1):
        def prxyx():
            result = 0
            for i in range(2):
                result += (X[i][0] + X[i][1])*pyx(1, y1)
            return result

        return ((X[1][0] + X[1][1]) * pyx(1, y1)) / prxyx()

    def prxxy(y2):
        def prxxyx():
            return X[1][1] * pyx(1, y2)

        def prxxyx_sum():
            result = 0
            for i in range(2):
                result += X[1][i] * pyx(i, y2)
            return result

        return prxxyx() / prxxyx_sum()

    return prxy(y[0]) * prxxy(y[1])


if __name__ == '__main__':
    data = DataSets(3, 3)
    data.create_data_sets(1)
    sg = Sg(data.sets[0]['y'], 3, 3, 1.0)
