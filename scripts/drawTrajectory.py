#! /usr/bin/python
import string
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__=='__main__':
#    trajectory = file('trajectory.txt')
    trajectory = file('/home/vance/slam_ws/ORB_SLAM2/Examples/Stereo/results/00/CameraTrajectory.txt')
    Fig = plt.figure(1)
    x = []
    y = []
    for line in trajectory:
        data = line.split()
        x.append( string.atof(data[1]) )
        y.append( string.atof(data[2]) )
    plt.plot( x, y, 'r-' )
    x = []
    y = []
    Fig.savefig("trajectory.png")
    Fig = plt.figure(2)
#    odo = file('odometry.txt')
    odo = file('/dataset/KITTI/poses/00.txt')
    for line in odo:
        data = line.split()
        x.append( -string.atof(data[2]))
        y.append( string.atof(data[8]))
    plt.plot( x, y, 'k-.')
    Fig.savefig("groundtruth.png")
