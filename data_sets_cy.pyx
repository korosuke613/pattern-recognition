from libc.stdlib cimport rand, RAND_MAX
from libc.math cimport sin, sqrt, log, M_PI
from libcpp.vector cimport vector

cdef int sdlab_random(int min_num, int max_num):
    return int(min_num + (rand()*(max_num-min_num+1.0)/(1.0+RAND_MAX)))

cdef double sdlab_uniform():
    cdef double ret
    ret = (rand() + 1.0) / (RAND_MAX + 2.0)
    return ret

cdef double sdlab_normal(double mu, double sigma):
    cdef double z
    z = sqrt(-2.0 * log(sdlab_uniform())) * sin(2.0 * M_PI * sdlab_uniform())
    return mu + sigma * z

cdef class DataSets:
    cdef int y1_num, y2_num
    cdef public list sets
    cdef double hensa

    def __init__(self, int y1_num, int y2_num):
        self.sets = []
        self.hensa = 1.0
        self.y1_num = y1_num
        self.y2_num = y2_num

    cdef tuple _create_x_tuple(self):
        cdef int r
        cdef tuple result
        r = sdlab_random(1, 100)
        if r < 60:
            result = (0, 0)
        elif r < 70:
            result = (0, 1)
        elif r < 80:
            result = (1, 0)
        else:
            result = (1, 1)
        return result

    cdef vector[double] _create_y_vec(self, int x, int y_num):
        cdef vector[double] y_tuple
        for _ in range(y_num):
            y_tuple.push_back(x + sdlab_normal(0.0, self.hensa))
        return y_tuple

    cdef list _create_y(self, int x, int y_num):
        cdef list y_tuple = []
        for _ in range(y_num):
            y_tuple.append(x + sdlab_normal(0.0, self.hensa))
        return y_tuple

    cdef tuple _create_y_tuple(self, tuple x_tuple):
        cdef tuple y
        cdef list y1, y2
        y1 = self._create_y(x_tuple[0], self.y1_num)
        y2 = self._create_y(x_tuple[1], self.y2_num)
        y = (y1, y2)
        return y

    cpdef void create_data_sets(self, int num=100000):
        cdef tuple x_tuple, y_tuple
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
