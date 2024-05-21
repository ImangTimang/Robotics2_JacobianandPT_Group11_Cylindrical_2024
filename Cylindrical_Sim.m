disp('Cylindrical Manipulator')
syms a1 a2 a3 t1 d2 d3

%% Link lengths
a1 = 3;
a2 = 3;
a3 = 3;

%% Joint Variables
d2 = 10;
d3 = 10;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta
H0_1 = Link([0,a1,0,0,0,0]);
H0_1.qlim = [-pi/2 pi/2];

H1_2 = Link([3*pi/2,0,0,3*pi/2,1,a2]);
H1_2.qlim = [0 d2];

H2_3 = Link([0,0,0,0,1,a3]);
H2_3.qlim = [0 d3];

Cyl = SerialLink([H0_1 H1_2 H2_3], 'name', 'Cyl')
Cyl.plot([0 0 0], 'workspace', [-5 8 -8 8 0 15])

figure(1)
Cyl.teach

%% Path and trajectory
%qpaths
t = 0:0.5:2
q0 = [0,0,0];   
q1 = [0 4 2.831];
q2 = [pi/2 4 2.831];
q3 = [pi 3 2.831];
q4 = [3*pi/2 2 2.831];
q5 = [2*pi 1.5 2.831];
q6 = [2*pi 0 0];

%trajectory
Traj1 = jtraj(q0,q1,t)
Traj2 = jtraj(q1,q2,t)
Traj3 = jtraj(q2,q3,t)
Traj4 = jtraj(q3,q4,t)
Traj5 = jtraj(q4,q5,t)
Traj6 = jtraj(q5,q6,t)

figure(2)
plot(Cyl,Traj1)
plot(Cyl,Traj2)
plot(Cyl,Traj3)
plot(Cyl,Traj4)
plot(Cyl,Traj5)
plot(Cyl,Traj6)
