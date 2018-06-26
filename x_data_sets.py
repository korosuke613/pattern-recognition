import random


class XDataSets:
    def __init__(self):
        self.sets = []

    @staticmethod
    def _create_data():
        r = random.randrange(100)
        if r <= 60:
            result = (0, 0)
        elif r <= 70:
            result = (0, 1)
        elif r <= 80:
            result = (1, 0)
        else:
            result = (1, 1)
        return result

    def create_data_sets(self, num=100000):
        for _ in range(num):
            self.sets.append(self._create_data())


def main():
    x_sets = XDataSets()
    x_sets.create_data_sets()
    pass


if __name__ == '__main__':
    main()
