# Autonomous Rescue Drone

Rescue plans generally last for days considering the current example of Turkey-Syria earthquake where death toll passed 28,000 as rescue hopes dwindle creating a critical shortcoming to the affected once. One of the major challenge is to find the survivors where at least 6,000 buildings collapsed in Turkey and victims are hoping for Miraculous rescues even after 100 hours under rubble. Quick disaster management system by the way of Autonomous Rescue Drones is the approach provide them help at the earliest, as delay may lead to rise in death toll. 

HARDWARE USED

1)Pixhawk 2.4.8 Drone Flight Controller PX4 32 Bit Autopilot

2)Q450 Quadcopter Frame – PCB Version Frame Kit with Integrated PCB

3)Orange HD Propellers 1045(10X4.5) ABS DJI Black 2CW+2CCW-2pair-Premium Quality

4)SimonK 30A BLDC ESC Electronic Speed Controller with Connectors

5)Raspberry Pi 4 Model B

6)Raspberry Pi Camera Module 3

7)A2212 1000 KV BLDC Brushless DC Motor for Drone (Soldered Connector)

8)3D Printed Legs for base

9)Converter for raspberry pi

10)FlySky FS-IA10B Radio Receiver

11)3300mAh 3S 11.1V Lithium polymer (LiPo) rechargeable battery with XT60 female connector 30C

12)Anti-Vibration Shock Absorber for APM/KK/MWC/PixHawk

13)FS-TH9X 2.4GHz 9CH Upgrade Transmitter 




Softwares: 

• Raspbian OS

• Command-line 

• Mission-planner 

• Q-ground Controller



Onboard electronics and sensors: 

• Receiver for manual controlling over transmitter

• Raspberry Pi - Model 4B 

• Pixhawk flight controller 

• GPS module and buzzer 

• Power distribution board 

• 12V - 5V DC-DC buck convertor 

• Ultrasonic sensor 

• Raspberry pi camera 

• Buzzer 

• Safety switch 

• Power distribution board 



Technical skills: 

• Basics of quadcopter kinematics and quadcopter autonomy. 

• Manual control of drone using receiver and transmitter

• ROS, Gazebo, PX4 

• Communication over MAVLINK between Raspberry Pi and Pixhawk 

• Image processing using OpenCV, and Raspberry pi 

• Human detection 

• soldering



The project can be split into THREE major categories – 

• Hardware and Instrumentation - The total assembly of the drone including the frame, battery, BMS, flight controller, GPS, onboard computer, camera, and other sensors. 

•Software for  Image Processing -Image processing for obstacles and human detection 

•Obstacle Avoidance & Path Planning - Operations to find the best possible route, the real-time scanning of the environment to detect any obstacles along the route.



A 32-bit headless Raspbian operating system is installed on Raspberry Pi, and it is configured to access over a secure shell (SSH) when raspberry pi is connected to a Wi-Fi network.Receiver-Transmitter is used for calibrating BLDC motors and manual flight control. 
MAVLINK protocol is used to communicate between Raspberry Pi and Pixhawk using a USB to the b-type serial communication port. 
A 12V to 5V DC-DC buck converter is used to power Raspberry Pi from Power Distribution Board (PDB). 
For image processing we have implemented an onboard RPI camera to take live footage using a python script and used Machine Learning algorithms to detect humans using OpenCV, NumPy, and hog features. • Along with human detection, our model is also capable of counting the number of people captured in the camera using the “putText’ function of OpenCV.


Challenges Faced:- 


1) Some installation issues with OpenCv, RaspberyPi and and got many errors while writing codes. 

2) Did some changes in the code files and changed the changed the software installed earlier.

3) One of the motor was not working properly so had faced difficulties in controlling the drone while takeoff. -Replaced the motor.

4) Compatibility issues with Raspbian OS versions and library installation.


