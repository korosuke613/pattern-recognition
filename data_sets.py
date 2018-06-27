import random


class DataSets:
    def __init__(self, y1_num, y2_num):
        self.sets = []
        self.hensa = 1.0
        self.y1_num = y1_num
        self.y2_num = y2_num

    @staticmethod
    def _create_x_tuple():
        r = random.randrange(100)
        if r < 60:
            result = (0, 0)
        elif r < 70:
            result = (0, 1)
        elif r < 80:
            result = (1, 0)
        else:
            result = (1, 1)
        return result

    def _create_y(self, x: int, y_num):
        y_tuple = []
        for _ in range(y_num):
            y_tuple.append(x + random.normalvariate(0.0, self.hensa))
        return y_tuple

    def _create_y_tuple(self, x_tuple):
        y1 = self._create_y(x_tuple[0], self.y1_num)
        y2 = self._create_y(x_tuple[1], self.y2_num)
        y = y1 + y2
        return y

    def create_data_sets(self, num=100000):
        for _ in range(num):
            x_tuple = self._create_x_tuple()
            y_tuple = self._create_y_tuple(x_tuple)
            self.sets.append({'x': x_tuple, 'y': y_tuple})


def main():
    data_sets = DataSets(3, 3)
    data_sets.create_data_sets()
    pass


if __name__ == '__main__':
    main()
