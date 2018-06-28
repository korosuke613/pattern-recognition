from data_sets_cy import DataSets
import matplotlib.pyplot as plt
from datetime import datetime
from tqdm import tqdm


cdef class ROC:
    cdef tuple xx
    cdef list roc
    cdef int y1_num, y2_num, num
    cdef double sigma

    def __init__(self, num=10000, y1_num=3, y2_num=3, sigma=1.0, xx=(1, 1)):
        self.y1_num = y1_num
        self.y2_num = y2_num
        self.num = num
        self.sigma = sigma
        self.xx = xx
        self.roc = []
        plt.xlim(0.0, 1.0)
        plt.ylim(0.0, 1.0)

    cdef int count_xx(self, list data):
        cdef dict e
        cdef int xx_num = 0
        for e in data:
            if e['x'] == self.xx:
                xx_num += 1
        return xx_num

    cdef create_S(self, object ss):
        cdef int i
        cdef list s
        cdef object data, sss

        data = DataSets(self.y1_num, self.y2_num)
        data.create_data_sets(self.num)
        s = []
        for i in range(self.num):
            sss = ss(data.sets[i]['y'], self.y1_num, self.y2_num, self.sigma)
            s.append(sss.get())
        return data.sets, s

    cpdef void calc_roc(self, object s):
        cdef int i
        self.roc = []
        for i in tqdm(range(101)):
            self.calc_roc_once(i / 100, s)

    cdef double FPR(self, int fp, int xx_num, s):
        return fp / (len(s) - xx_num)

    cdef double CDR(self, int cd, int xx_num):
        return cd / xx_num

    cdef void calc_roc_once(self, double threshold, object ss):
        cdef int xx_num, cd, fp, i
        cdef double a
        data, s = self.create_S(ss)
        xx_num = self.count_xx(data)
        cd = fp = 0
        for i, a in enumerate(s):
            if a >= threshold:
                if data[i]['x'] == (1, 1):
                    cd += 1
                else:
                    fp += 1
        self.roc.append((self.FPR(fp, xx_num, s), self.CDR(cd, xx_num)))

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
