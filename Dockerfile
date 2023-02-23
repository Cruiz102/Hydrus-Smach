FROM osrf/ros:melodic-desktop-full

# Install smach and smach_viewer
RUN apt update && apt install -y\
 ros-melodic-smach\
 ros-melodic-smach-ros\
 ros-melodic-executive-smach\
 ros-melodic-smach-viewer

RUN sudo apt install vim -y

# Install MoveIt and Build catkin workspace
RUN rosdep update
RUN sudo apt-get update
RUN sudo apt-get dist-upgrade
RUN sudo apt-get install ros-melodic-catkin python-catkin-tools

# Install MoveIt!
RUN apt install -y ros-melodic-moveit

#Create a Catkin Workspace
RUN mkdir -p ~/ws_moveit/src

#Dowload example packages
RUN cd ~/ws_moveit/src
RUN git clone https://github.com/ros-planning/moveit_tutorials.git -b melodic-devel
RUN git clone https://github.com/ros-planning/panda_moveit_config.git -b melodic-devel

#Build The Catkin Workspace
# RUN cd ~/ws_moveit
# RUN catkin config --extend /opt/ros/${ROS_DISTRO} --cmake-args -DCMAKE_BUILD_TYPE=Release
# RUN catkin build
RUN source ~/ws_moveit/devel/setup.bash

CMD . /opt/ros/melodic/setup.sh