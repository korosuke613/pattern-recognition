from roc import ROC
from statistics_cy import Sg, St, Sp
import matplotlib.pyplot as plt
from datetime import datetime

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)


def draw_roc_curve(roc, label='none', color='red'):
    x = [r[0] for r in roc]
    y = [r[1] for r in roc]
    plt.plot(x, y, color=color, label=label, lw=0.6)
    plt.legend(loc='lower right')


def save_roc_curve():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    plt.xlabel('FP(False Positive)')
    plt.ylabel('CD(Correct Detective)')
    plt.savefig('fig/' + timestamp + '.draw.pdf')
    plt.show()


def main():
    roc = ROC(num=100000)
    data = roc.calc_roc(Sg)
    draw_roc_curve(data, label='Sg', color='red')
    data = roc.calc_roc(St)
    draw_roc_curve(data, label='St', color='blue')
    data = roc.calc_roc(Sp)
    draw_roc_curve(data, label='Sp', color='green')
    save_roc_curve()


if __name__ == '__main__':
    main()
