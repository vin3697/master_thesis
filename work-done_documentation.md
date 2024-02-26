
**Work Done Documentation!**
```

=======================================================================================================================================

Date 3rd and 4th April

# http://wiki.ros.org/catkin/workspaces
- information regarding the folders such as 
src, devel, build and install space!


1. Installation of Linux system.(Dual booting my system)

2. Installation of ROS noetic system on host system.

3. Searched Research Paper

4. Meeting with Mr. Aboki dicussing more about the project.

5. Got information about the Human follower implementaion on internet.(Not the one implemented by research fellow's)

=======================================================================================================================================

Date 5th and 6th April.
- Installation of ROS noetic distro done


- Camera driver ( http://wiki.ros.org/kinect)
1. freenect_stack - http://wiki.ros.org/freenect_stack 

#openni is used!!!

2. openni - freenect_launch or openni_launch is the recommended package for using a Kinect with ROS.
http://wiki.ros.org/openni_launch
http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping

3. openni2 - It does NOT support any versions of the Kinect.
Kinect for Xbox 360: This uses openni driver package.

4. added https://github.com/ros-drivers/openni_camera package into the workspace 
 
   got error:
   Resource not found: rgbd_launch
   ROS path [0]=/opt/ros/noetic/share/ros
   ROS path [1]=/home/neox/catkin_ws/src
   ROS path [2]=/opt/ros/noetic/share
   The traceback for the exception was written to the log file
   solution: https://get-help.robotigniteacademy.com/t/resource-not-found-rgbd-launch-using-kinect-using-ros-noetic/12527

5. Read research paper
=======================================================================================================================================

Date 11th, 12th April

1. Searched research papers regarding navigation, sensor fusion.

2. Read some of the papers and documented them.

3. Particularly looking for papers where sensor fusion is done for Human awareness with navigation.

4. Looked for soultions with software.

=======================================================================================================================================


Date 13th April

1. Continued the work related to search of relevant research papers and possible different approaches regarding Thesis.

2. Found some good project implementation git repositories.

=======================================================================================================================================


Date 14th and 17th April

1. Gone through the Kinetic ROS driver/Package

2. Meeting with Mr. Aboki, and transfer of all workdone for human follower project.

3. Going through the research project report and understaning the source code/ nodes and their working.

=======================================================================================================================================

Date 18th April

1. Working with Bot.

2. In lab I worked with Mr. Aboki where we transffered and deployed the workspace for human follower.

3. Successfully executed the human follower demo.

=======================================================================================================================================

Date 19th April

1. Camera Calibration:

https://wiki.ros.org/openni_launch/Tutorials/IntrinsicCalibration

2. Going through the openni and RGBD ROS driver/packages 

3. Sucessfully calibrated the RBG camera but had problem with Depth Camera IR and was not able to calibrate it as blank image was displayed.
#   https://github.com/ros-drivers/openni_camera/issues/63

=======================================================================================================================================

Date 20th and 21st April

1. Tried to understand and find any article, research paper or any implementation were camera_angle was used for following the person.

2. Went through the work done by Sense : inference engine for action recognition.

3. Read Research papers where Openpose used.

4. Researched papers and read them.  

=======================================================================================================================================

Date 24th April

1. Tried to do camera calibaration with help of Freenect ROS driver.

	**installation of required package for Freenect to work!!** 
	https://rospibot.azw.pt/ros-noetic-kinect-xbox-360/

2. Went through research paper 

3. Understanding the source code developed for Human follower 
	- added comments to the source file identify_person.py
	- https://github.com/IntelRealSense/librealsense/issues/5553
	- https://stackoverflow.com/questions/17499409/opencv-calculate-angle-between-camera-and-pixel


4. https://linuxhint.com/checkout-specific-commit-git/
	worked with openpose ros package
=======================================================================================================================================

Date 25th April

1. Went to Logimat fare event.

=======================================================================================================================================

Date 26th till 28th April

1. I worked on installation of all required libraries and setting up the environment to build the OPenpose library.

2. After the build was succesful I started to work with ROS wrapper for Openpose and setting up the environment and specfic versions.

3. The software have issues with Ubuntu 20.04 system and Noetic ROS distro.

4. Found out other alternatives for openpose and sent to Mr. Aboki

=======================================================================================================================================

Date 3rd May till 7th May

1. Had meeting with Sharath and worked with his docker image.

2. I wanted different specifications for the image, so I created a new docker image with Ubuntu 18.04 , ROS distro : Melodic , Openpose and OPenpose ROS wrapper.

3. Succesfully tested it on my host system which has Ubuntu 20.04 Noetic ROS distro. 
(created a document named as : docker_image_creation refer to it)

=======================================================================================================================================

Date 8th May till 12th May

1. On the docker image, I installed Openni ROS driver : didnt work

2. Installed Frennect ROS driver it works on the Docker container.

3. Created the custom launch file for Kinect xbox depth camera.

4. Worked with it, but had issue where the ros-Openpose process dies.

5. Tired different ROSopenpose versions , but no luck. For some versions I had build errors which were new to the ROS openpose wrapper.

6. Tired to install the Azure kinect ROS driver but it didnt work as the device was not detectable, I tried this as the RAVI's repo had support for this driver.

7. Worked with the custom launch file but no luck. I tried to reduce the resoultion, use different models, and the changes where it could use the GPU VRAM as low as possible but no luck, so I raised the issue and as some parameters are missing its difficult to debug it.

8. Installed USB ROS driver, and tried working with USB cam. It works.

=======================================================================================================================================

Date 15th May till 19th May

1. Worked on configration of Custom Depth Camera and trying to resolve the issue wherer the ROS node/process is getting killed.

2. Raised the issue on Github

3. Got the reply, from repo owner, checked all other settings for it, still the issue persists.

4. Now instead of USB camera, I used the Kinect Camera ROS topic launching ROS openni driver from Host machine and launching ROS openpose from my docker container.

=======================================================================================================================================

Date 22 nd May till 26 May

1. worked on resolving the issue regarding the Ros-Openpose process.

2. Worked around with different openpose versions, making changes with launch files.

3. With trial and error and with combinations of different trys, got rid of that error.

4. RVIZ files were created to visualize the skeleton with RGB + Depth Image.

5. All these changes have been committed to the docker image created by me.

=======================================================================================================================================

Date 29th May till 2nd June

1. Worked with /frame topic and understanding it in a better way.

2. Started working on creation Gestures such as go_forward, go_backward, stop , go_right , and go_left.

3. Considered Pixel points instead of Point , for the Gesture defination.

4. Each day, worked with one of the Gesture and succesfully implemented it.

5. Starting working with publishing the velocity commands depending upon the Gesture.

=======================================================================================================================================

Date 5th June till 9th June

1. Worked with Robot testing and refining the Gesture to control the Robot.

2. Added two more Gestures to move robot forward + Turn.

3. Initially had problem with working Robot docker container and container developed my me.

4. The problem was resolved as ROS is distributed system we can have common master for n-number of nodes.

5. After resolving this above issue, I tested the point 1 and 2 as mentioned above.

=======================================================================================================================================

Date 12th June till 16th June

1. I tested my docker image and container on Mr. Nasiru's local system and works smooth.

2. Went back again to do some research with pose estimantion and Openpose.

3. Found papers where by using Openpose posture was estimated.

4. Started basic implementation with my understaning.

=======================================================================================================================================

Date 19th June till 23rd June

1. The posture for sitting was fisnished with some mathematical logic.

2. To sitting posture itself added some more conditions to make it robost.

3. Implemented it with the robot and tested.

4. Added the custom message where the information is provided about the posture.

=======================================================================================================================================

Date 26th June till 30th June

1. Added more features to the posture such as facing backwards, facing side ways and facing towards.

2. Did some refinement with the gesture control script added some more conditions.

3. Tested the new added features for the posture with executing it with the Robot in the office.

=======================================================================================================================================

Date 3rd July till 7th July

1. Added safety feature into the gesture control script, making it more safe and added gestures for the same.

2. Did research on Use cases which can be implemented in our indoor office environment.

=======================================================================================================================================

Date 10th July till 14th July

1. Camera is not mounted on Robot so not worth doing VSLAM (USE case : To locate a person and visit him/her)

2. Did research regarding which algorithms can be implemented for Navigation with help of 2D lidar. [Gmapping or Cartographer]

3. Had idea to implement the BUG algorithms to avoid obstacles. (which doesnt needs any mapping, its a run time algorimth)

4. The problem with the BUG algorithm is we have to give a location in co-ordinate form for which we will need some kind of map.

5. Researched about the problems we are facing.

=======================================================================================================================================

Date 17th July till 21th July

1. Researched on optical flow and SLAM + Pose estimation for locate the target and give it as goal.

2. Researched on getting the 3D co-ordinates from Camera frame to Map frame and localizing the robot while Navigation stack being used.

3. Researched on VSLAM (RTAB), due to the time constraint it hardly possible to implement it and fine tune it.

4. To implement the VSLAM, the kinect sensor made it more diffcult to implement(if possible) so found some articles regarding same.
   The articles were regarding using a power supply of 12v and working around with the wiring of Kinect Camera sensor.

5. Documented the wiring of Kinect sensor, so in future we might have to do the modifications.
     
=======================================================================================================================================

Date 24th July till 28th July

1. Again did some research regarding the SLAM algorithms (mostly : Gmapping, Cartographer and Hector SLAM)

2. Selected Hector as final SLAM in implementation, as it was fine tunned and to go with Cartographer it would be really hard to go through it and fine tune it.

3. Did a research overview how actually Hector SLAM works(not going into detailed parameters of it)

4. Went throught the documentation of RPI4 to run Linux image and Lidar to understand basic functioning.

5. As, Hector SLAM was finilized, started implementing it. (making my own workspace and transfering navigation stack fine tunned parameters).

6. Made changes in the URDF file of Ohmni robot where the position of Lidar was corrected.

7. Had to adjust the height of lidar on Robot, to get a well map of surroundings.

8. Redefined some of the launch files (move_base and YD lidar)

9. Created new maps of the lab, and did navigation by giving goal. (observed the recovery behaviour as well)


=======================================================================================================================================

Date 31st July till 4th August and Date 7th July till 11th August

1. Started working on Navigation Stack (AMCL : Localisation and Move_Base for Navigation)

2. Dived deep into the Navigation Stack which was implemented by fellow members.

3. Worked extensievly with the Cost Map parameters(Common, Global and Local) and DWA local planner parameters.

4. Started cleaning the Navigation stack, removed unnecessary files and parameters which made the Navigation Stack really complicated.

5. Referred to some Robot's Navigation stack and tired to implement them (which were similar to the Navigation stack implemented by my fellow team mates)

6. But the DWA local planner was not able to create a plan and was going into recovery mode.

7. Went through documentation of parameters and tried different combinations.

8. Finaly got the right parameters and Robot was able to Navigate thorugh the Map quite efficiently w.r.t previous implemnetations.

9. Added necessary explanation for the parameters into the files with relevant links.

10. Started to tune the parameters and going more deep into them.

11. Footpirnt for the Robot was fixed. [Actual size of Robot while Navigating which is imp paramter and hardly anyone had worked on it]

=======================================================================================================================================

Date 14th August till 18th August

1. Started working on the use case.

2. Worked with creation of python script for Navigation stack, using MoveBase package and succesfully tested it.

3. Defined a new message for the use case, which includes the person ID, Posture, Facing and Gesture for Obey, Disobey, LocationA and LocationB.

4. Refining of above scripts was done in this week later.

=======================================================================================================================================

Date 21st August to 25th August

1. Tested the above scripts with Openpose + Navigation stack.

2. Did some more refinment in the source codes.

3. Pushed everything related to Openpose to the Docker hub.

4. Worked around with synchornisation of Time on both systems, as there was problem between the tf recieved from Robot and which were intergrated with tf from robot description.

5. Tried different ways of synchronizing the time, but hardly of them worked.

6. Robot's battery must be fully charged for its smooth fucntioning (above 85%)

=======================================================================================================================================

Date 28th August to 1st September

1. Worked on Time synchronization for Docker containers to have same as Host.

2. Tested Openpose software(Docker Container) with the Camera powered by power bank.

3. Started working on the Navigation stack. (varying some parameters as the time snyc is causing the delay TF problem due to which Navigation is getting affected)

4. Execution and testing of USE Case (Openpose + Navgiation Stack) [camera powered by power bank]

=======================================================================================================================================

Date 4th September onwards!

1. Started working with the Master Thesis Report.

2. Integrated LaTex with VScode.

3. Started working with Zotero.

4. Went through IAAS documentation of writing scientific papers

=======================================================================================================================================

```


















