#! /usr/bin/python
import string
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
    # draw ground_truth
    ground_truth = open('/home/vance/dataset/kitti/poses/07.txt')
    x_gt = []
    y_gt = []
    z_gt = []
    for line in ground_truth:
        data = line.split()
        x_gt.append(float(data[3]))
        y_gt.append(float(data[7]))
        z_gt.append(float(data[11]))
    p1, = plt.plot(x_gt, y_gt, 'k-', label='ground truth')
    # plt.show()

    # draw trajectory
    trajectory = open('/home/vance/dataset/kitti/results/kitti_trajectory_07.txt')
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
#    plt.xlim(-140,20)
#    plt.ylim(-80,20)
    p2, = plt.plot(x_t, y_t, 'b.', label='trajectory')
    p3, = plt.plot(x_t[0], y_t[0], 'ro')
#    p4, = plt.plot(x_t[num-1], y_t[num-1], 'yo')
    plt.legend([p1, p2, p3], ['ground truth', 'trajectory', 'start'], loc=0)
    plt.show()

    # Fig.savefig("result.png")
