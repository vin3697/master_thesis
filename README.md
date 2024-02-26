----------------------------------------------------------------------------------------------------

					|   Its Important You go through the Thesis Report very well!     |
					|             To Understand following Commands                    |
					|   Every thing is explained very well in Thesis Report ;-)       |
											
----------------------------------------------------------------------------------------------------

# Docker Hub - Image

Openpose work is pushed to Docker Hub in Docker Image form : https://hub.docker.com/r/vin8/openpose_vin       



# Connecting to Robot.
```
NOTE : IP addresses might change, please check them!
IP address of Butler BOT  : 129.69.207.64 
IP address of Local HOST  : 129.69.207.127

localhost@shell:~$ adb connect 129.69.207.64
localhost@shell:~$ adb disconnect 129.69.207.64

ButtlerBot@shell:~$ adb shell
ButtlerBot@shell:~$ su
ButtlerBot@shell:~$ setprop ctl.stop tb-node
```

Already Docker Container is available, just RUN it.
```
ButtlerBot@shell:~$ docker start container_name
ButtlerBot@shell:~$ docker attach container_name
ButtlerBot_docker@shell:~# rostopic list
```
----------------------------------------------------------------------------------------------------

Open new Terminal on Local System : Important to connect to the ROS Master from Multiple Machines.
```
localhost@shell:~$ export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
```

Check on Local system, are you able to get the ROS topics from Robot, 
if Yes then you have succesfully established the communication with Robot throught your Local System.
```
localhost@shell:~$ rostopic list
```


----------------------------------------------------------------------------------------------------

#													Time Sync
```
localhost@shell:~$ timedatectl
ButtlerBot_docker@shell:~# timedatectl
```
Synchronize the Time between Robot Machine and Local System Machine.
First use the below command to bring both system in same time zone.
```
@shell:~$ sudo dpkg-reconfigure tzdata
```

## Commands on Robot
```
ButtlerBot_docker@shell:~# sudo /etc/init.d/chrony restart
ButtlerBot_docker@shell:~# sudo initctl restart chrony
ButtlerBot_docker@shell:~# sudo systemctl enable chrony
```

## Commands on Laptop
```
localhost@shell:~$ sudo systemctl restart chrony
localhost@shell:~$ sudo systemctl status chrony
localhost@shell:~$ sudo systemctl enable chrony
```

----------------------------------------------------------------------------------------------------

# 													Navigation Stack + Openpose(Gesture+Posture Knowledge)

Open new Terminal on Local System : Important to connect to the ROS Master from Multiple Machines.
```
localhost@shell:~$ export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
localhost@shell:~$ roslaunch ohmni_2dnav ohmni_nav.launch 
```
New Terminal to RUN ROS Visualization.
```
localhost@shell:~$ export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
localhost@shell:~$ rosrun rviz rviz -d /home/user_name/path_to_RVIZ_file/SLAM_ws/src/ohmni_2dnav/src/config/rvizconfig.rviz 
```
OPENPOSE.
```
localhost@shell:~$ sudo xhost +si:localuser:root

localhost@shell:~$ docker run --gpus all -e DISPLAY=$DISPLAY --env NVIDIA_VISIBLE_DEVICES=all --env NVIDIA_DRIVER_CAPABILITIES=all --env DISPLAY --env QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev:/dev --net=host --privileged --device=/dev/video0:/dev/video0 -it vin8/openpose_vin:final /bin/bash
```
Once Docker Image instance is created, just work around with that Docker Container.
```
localhost@shell:~$ docker start openpose_container_name; docker attach openpose_container_name
```
inside container.
```
openpose_docker@shell:~# export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
openpose_docker@shell:~# roslaunch ros_openpose run.launch
```
Open New Terminal to RUN ROS node for setting the Goal through Gesture recognization.
```
localhost@shell:~$ docker exec -it openpose_container_name /bin/bash
openpose_docker@shell:~# export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
openpose_docker@shell:~# rosrun ros_openpose set_goal.py 
```
New Terminal to RUN ROS node for Gesture-based Navigation.
```
localhost@shell:~$ export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
localhost@shell:~$ rosrun ohmni_2dnav gesture_goal_nav.py
```
----------------------------------------------------------------------------------------------------

#													Gesture-based Robot control

OPENPOSE
```
localhost@shell:~$ sudo xhost +si:localuser:root
```
Once Docker Image instance is created, just work around with that Docker Container.
```
localhost@shell:~$ docker start openpose_container_name; docker attach openpose_container_name
```
inside container
```
openpose_docker@shell:~# export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
openpose_docker@shell:~# roslaunch ros_openpose run.launch
```
Open New Terminal to RUN ROS node for controlling the Robot via Gestures.
```
localhost@shell:~$ docker exec -it openpose_container_name /bin/bash
openpose_docker@shell:~# export ROS_IP=129.69.207.127; export ROS_MASTER_URI=http://129.69.207.64:11311
openpose_docker@shell:~# rosrun ros_openpose gesture_ctrl.py 
```
----------------------------------------------------------------------------------------------------
























