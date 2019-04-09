#! /usr/bin/python
import string
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    # draw trajectory
    trajectory = open('/home/vance/dataset/fzu/results/trajectory.txt')
    x_t = []
    y_t = []
    z_t = []
    num = 0
    for line in trajectory:
        data = line.split()
        x_t.append(float(data[11]))
        y_t.append(-float(data[3]))
        z_t.append(float(data[7]))
        num += 1
    plt.xlim(-140,20)
    plt.ylim(-80,20)
    p1, = plt.plot(x_t, y_t, 'b-', label='trajectory')
    p2, = plt.plot(x_t[0], y_t[0], 'ro')
    p3, = plt.plot(x_t[num-1], y_t[num-1], 'yo')
    plt.legend([p1, p2, p3], ['trajectory', 'start', 'end'], loc=0)
    plt.show()

#    Fig.savefig("result.png")
