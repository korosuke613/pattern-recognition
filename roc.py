from data_sets_cy import DataSets
from statistics_cy import Sg, St, Sp
import matplotlib.pyplot as plt
from datetime import datetime
from tqdm import tqdm


class ROC:
    def __init__(self, num=10000, y1_num=3, y2_num=3, sigma=1.0, xx=(1, 1)):
        self.y1_num = y1_num
        self.y2_num = y2_num
        self.num = num
        self.sigma = sigma
        self.xx = xx
        self.roc = []
        plt.xlim(0.0, 1.0)
        plt.ylim(0.0, 1.0)

    def count_xx(self, data):
        xx_num = 0
        for e in data:
            if e['x'] == self.xx:
                xx_num += 1
        return xx_num

    def create_S(self, ss):
        data = DataSets(self.y1_num, self.y2_num)
        data.create_data_sets(self.num)
        s = []
        for i in range(self.num):
            sss = ss(data.sets[i]['y'], self.y1_num, self.y2_num, self.sigma)
            s.append(sss.get())
        return data.sets, s

    def calc_roc(self, s):
        self.roc = []
        for i in tqdm(range(101)):
            self.calc_roc_once(i / 100, s)

    def calc_roc_once(self, threshold, ss):
        def FPR():
            return fp / (len(s) - xx_num)

        def CDR():
            return cd / xx_num
        data, s = self.create_S(ss)
        xx_num = self.count_xx(data)
        cd = fp = 0
        for i, a in enumerate(s):
            if a >= threshold:
                if data[i]['x'] == (1, 1):
                    cd += 1
                else:
                    fp += 1
        self.roc.append((FPR(), CDR()))

    def draw_roc_curve(self, label='none', color='red'):
        x = [r[0] for r in self.roc]
        y = [r[1] for r in self.roc]
        plt.plot(x, y, color=color, label=label, lw=0.6)
        plt.legend(loc='lower right')

    @staticmethod
    def save_roc_curve():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plt.xlabel('FP(False Positive)')
        plt.ylabel('CD(Correct Detective)')
        plt.savefig('fig/' + timestamp + '.draw.pdf')
        plt.show()


def main2():
    roc = ROC(num=100000)
    roc.calc_roc(Sg)
    roc.draw_roc_curve(label='Sg', color='red')
    roc.calc_roc(St)
    roc.draw_roc_curve(label='St', color='blue')
    roc.calc_roc(Sp)
    roc.draw_roc_curve(label='Sp', color='green')
    roc.save_roc_curve()


if __name__ == '__main__':
    main2()