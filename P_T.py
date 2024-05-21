import roboticstoolbox as rtb
import math
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3

## Create Model
# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# link conversion to meter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2) 
a3 = mm_to_meter(a3) 
 
# link limits converted to meter (d1)
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)

lm2 = float(input("lm2 = "))
lm2 = mm_to_meter(lm2)
# Create links
# [robot_variable]=DHRobot([RevoluteDH(d,r,alpha,offset=theta,qlim)])
# [robot_variable]DHRobot([PrismaticDH(d=0,r,alpha,offset=d,qlim)])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
Cylindrical = DHRobot([
    RevoluteDH(a1,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    PrismaticDH(0,0,(270.0/180.0)*np.pi,a2,qlim=[0,lm1]),
    PrismaticDH(0,0,(0.0/180.0)*np.pi,a3,qlim=[0,lm2]),
], name="Cylindrical")

print(Cylindrical)


def deg_to_rad(T):
    return (T*np.pi)/180

q0 = np.array([0,0,0])

q1 = ([deg_to_rad(float(input("t1 = "))),
       mm_to_meter(float(input("d2 ="))),
       mm_to_meter(float(input("d3 =")))])

q2 = ([deg_to_rad(float(input("t1 = "))),
       mm_to_meter(float(input("d2 ="))),
       mm_to_meter(float(input("d3 =")))])

q3 = ([deg_to_rad(float(input("t1 = "))),
       mm_to_meter(float(input("d2 ="))),
       mm_to_meter(float(input("d3 =")))])

traj1 = rtb.jtraj(q0,q1,20)
traj2 = rtb.jtraj(q1,q2,20)
traj3 = rtb.jtraj(q2,q3,20)

x1 = -0.1
x2 = 0.1
y1 = -0.1
y2 = 0.1
z1 = 0.0
z2 = 0.1


Cylindrical.plot(traj1.q,limits=[x1,x2,y1,y2,z1,z2])
Cylindrical.plot(traj2.q,limits=[x1,x2,y1,y2,z1,z2])
Cylindrical.plot(traj3.q,limits=[x1,x2,y1,y2,z1,z2],block=True)