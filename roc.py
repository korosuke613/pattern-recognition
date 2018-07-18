from data_sets_cy import DataSets
from statistics_cy import Sg, St, Sp12, Sp21
import matplotlib.pyplot as plt
from datetime import datetime
from tqdm import tqdm
import numpy as np


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
        _d = np.array(data.sets)
        _s = np.array(s)
        return np.vstack((_d, _s))

    def create_Ss(self, ss1, ss2):
        data = DataSets(self.y1_num, self.y2_num)
        data.create_data_sets(self.num)
        s = []
        for i in range(self.num):
            sss1 = ss1(data.sets[i]['y'], self.y1_num, self.y2_num, self.sigma)
            sss2 = ss2(data.sets[i]['y'], self.y1_num, self.y2_num, self.sigma)
            if sss1.prX1GivenY1(sss1.get_n()) < sss2.prX1GivenY1(sss2.get_n()):
                sss = sss1
            else:
                sss = sss2
            s.append(sss.get())
        _d = np.array(data.sets)
        _s = np.array(s)
        return np.vstack((_d, _s))

    def calc_roc_Ss(self, ss1, ss2):
        def FPR():
            return fp / (len(data[1]) - xx_num)

        def CDR():
            return cd / xx_num
        self.roc.clear()
        data = self.create_Ss(ss1, ss2)
        xx_num = self.count_xx(data[0])
        index = np.argsort(data[1])
        cd = fp = already_x = count = 0
        for i in tqdm(index):
            if data[0][i]['x'] == (1, 1):
                already_x += 1
            cd = xx_num - already_x
            fp = self.num - count - cd
            self.roc.append((FPR(), CDR()))
            count += 1

    def calc_roc(self, ss):
        def FPR():
            return fp / (len(data[1]) - xx_num)

        def CDR():
            return cd / xx_num
        self.roc.clear()
        data = self.create_S(ss)
        xx_num = self.count_xx(data[0])
        index = np.argsort(data[1])
        cd = fp = already_x = count = 0
        for i in tqdm(index):
            if data[0][i]['x'] == (1, 1):
                already_x += 1
            cd = xx_num - already_x
            fp = self.num - count - cd
            self.roc.append((FPR(), CDR()))
            count += 1

    def draw_roc_curve(self, label='none', color='red'):
        x = [r[0] for r in self.roc]
        y = [r[1] for r in self.roc]
        plt.plot(x, y, color=color, label=label, lw=0.6)
        plt.legend(loc='lower right')

    def save_roc_curve(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plt.xlabel('FP(False Positive)')
        plt.ylabel('CD(Correct Detective)')
        plt.title(f"y1_num={self.y1_num}, y2_num={self.y2_num}, times={self.num}")
        plt.savefig('fig/' + timestamp + '.draw.pdf')
        plt.show()


def main2():
    roc = ROC(num=100000, y1_num=3, y2_num=3)
    roc.calc_roc(Sg)
    roc.draw_roc_curve(label='Sg', color='red')
    roc.calc_roc(St)
    roc.draw_roc_curve(label='St', color='blue')
    roc.calc_roc(Sp12)
    roc.draw_roc_curve(label='Sp1→2', color='green')
    #roc.calc_roc(Sp21)
    #roc.draw_roc_curve(label='Sp2→1', color='orange')
    roc.calc_roc_Ss(Sp12, Sp21)
    roc.draw_roc_curve(label='Ss', color='black')
    roc.save_roc_curve()


if __name__ == '__main__':
    main2()