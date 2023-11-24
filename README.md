This is the first task of my second year enternship, in wich i learned the basics of ROS and to program the protocol publisher-subscriber as showing the diagram

![ros publisher subscriber](https://github.com/med0amine/ros-publisher-and-subscriber/blob/main/images/ros%20publisher%20subscriber.png)


the steps of installing ROS melodic in Ubuntu as well as setting up the publisher and subscriber nodes are showing down bellow 
## installation of ROS
1. Setup of sources.list
~~~
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
~~~
2. Set up of keys
~~~
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
~~~
3. Installation
~~~
sudo apt update
sudo apt install ros-noetic-desktop-full
~~~
4. Environment setup
~~~
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
~~~
5. Dependencies for building packages
~~~
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
~~~
- Initializing rosdep
~~~
sudo rosdep init
rosdep update
~~~
6. Create catkin workspace
~~~
$ source /opt/ros/noetic/setup.bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
source devel/setup.bash
~~~
7. Create a ROS package
~~~
$ cd ~/catkin_ws/src
$ catkin_create_pkg pub_and_sub std_msgs rospy roscpp
$ cd ~/catkin_ws
$ catkin_make
$ source devel/setup.bash
~~~
## Create a ROS publisher and subscriber
- Create the publisher node
~~~
$ cd ~/catkin_ws
$ source devel/setup.bash
$ cd src
$ roscd pub_and_sub
$ mkdir scripts
$ cd scripts/
$ touch talker.py
$ vim talker.py
$ chmod +x talker.py 
~~~
- Create the subscriber node
~~~
$ cd ~/catkin_ws
$ source devel/setup.bash
$ cd src
$ roscd pub_and_sub/scripts
$ touch reciever.py
$ vim reciever.py
$ chmod +x reciever.py 
~~~
- Launch roscore
~~~
$ cd ~/catkin_ws
$ source devel/setup.bash
$ roscore
~~~
- Launch the publisher node
~~~
$ cd ~/catkin_ws
$ source devel/setup.bash
$ rosrun pub_and_sub talker.py
~~~
- Launch the subscriber node
~~~
$ cd ~/catkin_ws
$ source devel/setup.bash
$ rosrun pub_and_sub reciever.py
~~~

For more information you can visit: http://wiki.ros.org/ 
