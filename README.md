

![JACOBIAN AND PATH TRAJECTORY (1)](https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/a86ae340-967b-492b-a210-2f10985c2189)

###

 <h2 align="center"> ˚ ༘♡ ⋆｡˚Abstract of the Project	

 ###
 This section will discuss the topics of Jacobian matrix, singularities, differential equations, and path and trajectory planning for cylindrical manipulators, all of which are essential for meeting the Final Requirements in Robotics 2. Industrial fields commonly use cylindrical manipulators because of their simple structure, ease of use, and controllability. For this, we start by calculating the Jacobian matrix for a cylindrical manipulator and then creating a graphical user interface (GUI) to verify the accuracy of the answers. We highlight the significance of the Jacobian matrix in calculating both the joint and end-effector velocities. The investigation continues with the identification and classification of determinants using the basket method to determine the singularities within the manipulator's workspace, as well as their implications for motion planning and control strategies. We develop differential equations that govern the manipulator's dynamics, establishing the foundation for comprehending its behavior under diverse operating conditions. We then focus on path and trajectory planning, using the Jacobian matrix to create algorithms that ensure smooth, collision-free motion. Simulations using a virtual machine and MATLAB validate the proposed methodologies, showcasing their effectiveness in enhancing manipulator performance. The findings help to optimize cylindrical manipulator operations and provide insights into advanced robotic system design and control.

 
###
![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###

 <h2 align="center"> ˚ ༘♡ ⋆｡˚Introduction of the Project	
   
###
   
  The field of robotics has seen significant advancements in recent decades, with manipulators playing a crucial role in various industrial applications. Among these, cylindrical manipulators are particularly noteworthy due to their simplicity, reliability, and ease of control. Tasks such as assembly, welding, and material handling extensively use these manipulators, characterized by their cylindrical coordinate system. Understanding and optimizing their performance necessitates a thorough examination of several key concepts, including the Jacobian matrix, singularities, differential equations, and path and trajectory planning.

The Jacobian matrix is fundamental in robotics, providing a mathematical tool that relates the joint velocities of a manipulator to its end-effector velocities. This relationship is critical for a manipulator to fully understand the motion and control required for its proper function. When the Jacobian matrix loses rank at determinant points in the manipulator's workspace, there are problems like joint speeds that never end and losing control. Identifying and managing these singularities is essential for ensuring safe and efficient operation.
Differential equations govern the dynamics of cylindrical manipulators, describing how they respond to various forces, velocities, and torques. These equations form the basis for developing control strategies that can predict and influence the manipulator's behavior. Effective path and trajectory planning further enhances the manipulator's performance, enabling it to execute precise and smooth movements while avoiding obstacles and singularities and making a collision-free motion.
This paper aims to provide a detailed analysis and lessons from these interconnected aspects. We start by deriving the Jacobian matrix for a cylindrical manipulator and exploring its properties. Next, we identify singularities by solving the determinants within the workspace and discussing their implications. We then formulate the differential equations that describe the manipulator's dynamics, setting the stage for advanced control techniques. Finally, we delve into path and trajectory planning, presenting algorithms that leverage the Jacobian matrix to achieve optimal motion planning. Aside from this, we also formulate a GUI calculator that everyone can use to check values for this Jacobian matrix. Through simulations, we validate our approaches, demonstrating their practical applicability and effectiveness.

By integrating these key concepts, this paper contributes to the broader understanding and enhancement of cylindrical manipulator operations. We aim to use the insights gained here to develop robotic systems that are more efficient, reliable, and versatile, thereby advancing the field of industrial automation.	

![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###
 <h2 align="center">  ˚ ༘♡ ⋆｡˚ Jacobian Matrix of A Cylindrical Manipulator	

 ###


↳ DESCRIPTION ༉‧₊

Carl Gustav Jacob Jacobi, a German Jewish mathematician, first introduced the concept matrix in the 19th century. A key idea in engineering and robotics, the Jacobian matrix illustrates how a robot's kinematics vary with its joint coordinates. A matrix of partial derivatives of the end-effector's position vector with respect to the robot's joint coordinates is known as a Jacobian matrix. Stated differently, it explains how minute adjustments to the robot's joint angles impact the end-effector's location and orientation. The joint movements denote the rotational speed (for revolute joints) or extension/contraction rate (for prismatic joints) of each joint in the robot's arm. The end-effector movement describes the end-effector's linear and angular velocities (or positions), indicating how fast and in which direction it is moving (or positioned). Numerous robotics applications, including force control, trajectory generation, and path planning, make use of the Jacobian matrix.

**`·..➭ Solution**

<p align="center">	
<img width= "600" src="https://github.com/ImangTimang/Robotics2_JacobianMatrix_Group11_Cylindrical_2024/assets/157549014/1451342c-4943-4420-95cc-d1cbcd56f701">
</p>

####

###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT JACOBIAN MATRIX OF A CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>


###
<p align="center">
  <img width="600" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/d7d3f0a0-b740-415f-ae67-8b37f9fe92e6">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1RwFUqLyawf1-Sa65ilDZdzARyNfDDnqz/view?usp=sharing" target="_blank">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>


![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###

 <h2 align="center">  ˚ ༘♡ ⋆｡˚ Differential of A Cylindrical Manipulator	

###
↳ DESCRIPTION ༉‧₊


###

  A matrix of partial derivatives of the functions in the differential equation system is called the Jacobian matrix. Every point at which f is differentiable is represented by its differential. The partial derivatives of the functions with regard to joint displacements make up the matrix. The differential relationship between the joint displacements and the end-effecter motion that results is represented by the Jacobian matrix.
  
###
<p align="center">	
<img width= "600" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157492494/d3d1fcc8-f58c-400e-9719-3103e4ebbe6b"
>
</p>

###

###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT SOLIVING DIFFERENTIAL OF A CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>


###
<p align="center">
  <img width="450" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/7ea4865f-285b-4629-9bb2-0b34ff28d001">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1UEQEia1BO-khNH4GyKFKjLKaIGJZtx8d/view?usp=sharing">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

#

###
**»SINGULARITY IN JACOBIAN MATRIX OF A CYLINDRICAL MANIPULATOR**
###
↳ DESCRIPTION ༉‧₊


###
  A singularity is a location in a robot's workspace where one or more degrees of freedom (DoF) are lost. A robot will either cease moving or move in an unanticipated way when its tool center point (TCP) approaches or enters a singularity.

  Recall that the number of independently programmable joints on a robot equals its degree of freedom (DoF). Therefore, a 6 DoF robot has six independently moveable joints, as do the majority of industrial robots. A 6 DoF robot will effectively become a 4 or 5 DoF robot when it enters a singularity, destroying one or more of its joints.

###
###
<p align="center">	
<img width= "450" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157492494/0f923cce-fd1c-4c7c-87f9-9ce0b7d281cf"

</p>

###

<p align="center">
	
_FOR MORE EXPLANATION ABOUT SOLIVING THE SINGULARITY OF A CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>


###
<p align="center">
  <img width="450" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/20db94b7-1d0e-4eff-b19c-38a232045ec6">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1Y0DEln8zlDV0JO0G9CBBlWBTAvE9OP5q/view?usp=sharing">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###
 <h2 align="center">  ˚ ༘♡ ⋆｡˚ Jacobian Matrix of A Cylindrical Manipulator	

 ###


↳ DESCRIPTION ༉‧₊


###

Important topics in the fields of robotics and automation more broadly are path planning and trajectory planning. In fact, in order to attain shorter production times, robots and autonomous machines are trending toward operating at ever-higher speeds. Due to the high operating speed, which might cause extreme performances from the actuators and control system, the robot motion's repeatability and accuracy may be compromised. As a result, extra care should be taken to create a trajectory that can be followed quickly without endangering the robot by preventing excessive actuator accelerations and mechanical structure vibrations. A trajectory like that is said to be smooth. Because of these factors, trajectory planning and path planning

#

###
![436522470_416134364639675_2691159275235051753_n](https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/a7e6e72d-9756-4915-8ba1-ce414c8a64b4)

![445821114_1120735622448622_8263710956215963568_n](https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/9f39bfd0-edf8-4977-9080-9c0cd8575496)

![436013294_374045945106336_1395162898234613610_n](https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/12fcdb24-65d0-4d73-a2f4-e2aad98e4ea0)

![442660643_1004688993833393_540490273657018131_n](https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/38a6e923-43d3-4763-90d9-5218ab6fb05a)

![442705760_465351759347703_5441534518094845501_n](https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/bceece20-0a17-444d-b1e6-51198e2d0c00)

#
###
<p align="center">
	
_FOR MORE EXPLANATION ABOUT PATH AND TRAJECTORY OF A CYLINDRICAL MANIPULATOR WATCH THE VIDEO:_

</p>


###
<p align="center">
  <img width="450" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/41fed9f2-bacc-49a5-a26e-87c64a1422a9">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/1WGj0_jPVVt4iLAymyieFgx-H6kolkVqW/view?usp=sharing">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>

###
#
###
**»PATH AND TRAJECTORY GUI CALCULATOR OF A CYLINDRICAL MANIPULATOR**
###
↳ VIDEO ༉‧₊

### 
GUI CALCULATOR 

<p align="center">
  <img width="450" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157549014/e0b46ace-5ba6-444d-b5ac-107f5effa95a">
</p>



###
<p align="center">
  <img width="450" src="https://github.com/ImangTimang/Robotics2_JacobianandPT_Group11_Cylindrical_2024/assets/157728066/32c78e34-0e25-4607-a2b4-e779256a1542">
</p>

<div align="center">
  <a href="https://drive.google.com/file/d/17DNjmEMWn0cY3oTHavFcX-kmk4GRZIcC/view?usp=sharing">
    <img height=100" src="https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/0d3c379c-6cbe-42fb-ab1a-b4c7201f76bc"  />
  </a>
</div>


![R (4)](https://github.com/ImangTimang/Cylindrical_Manipulator_Testing/assets/157728066/15d3dfb1-d0e8-4dc7-8f99-bdefd5121fea)

###
 <h2 align="center">  ˚ ༘♡ ⋆｡˚ REFERENCES	

 ###

		https://robodk.com/blog/robot-singularities/
		https://www.mathworks.com/help/matlab/ref/odejacobian.html
  		https://www.researchgate.net/publication/282955967_Path_Planning_and_Trajectory_Planning_Algorithms_A_General_Overview
  		

 
