from roc_cy import ROC
from statistics_cy import Sg, St, Sp


def main():
    roc = ROC(num=100000)
    roc.calc_roc(Sg)
    roc.draw_roc_curve(label='Sg', color='red')
    roc.calc_roc(St)
    roc.draw_roc_curve(label='St', color='blue')
    roc.calc_roc(Sp)
    roc.draw_roc_curve(label='Sp', color='green')
    roc.save_roc_curve()


if __name__ == '__main__':
    main()
