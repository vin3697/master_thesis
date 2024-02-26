#!/usr/bin/env python


import rospy
import geometry_msgs.msg
from ohmni_2dnav.msg import PostureGesture
from actionlib_msgs.msg import GoalStatus
import actionlib
from   move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import tf


class realtimeController():

    def publishMoveBase(self, l_x, l_y, l_yaw):

        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"     
        goal.target_pose.header.stamp = rospy.Time.now()
        goal.target_pose.pose.position.x = l_x 
        goal.target_pose.pose.position.y = l_y
        #TODO : get the x,y,yaw from Desk varaible properly
        x , y, z, w = tf.transformations.quaternion_from_euler(0, 0, l_yaw)
        goal.target_pose.pose.orientation.x = x
        goal.target_pose.pose.orientation.y = y
        goal.target_pose.pose.orientation.z = z
        goal.target_pose.pose.orientation.w = w
        goal_client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
        goal_client.wait_for_server()
        # publish the goal to the topic
        goal_client.send_goal(goal)

        wait = goal_client.wait_for_result()
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
        else:
            return goal_client.get_result()


def controller_callback():
    #   1) X coordinate in the map in meters
    #   2) Y coordinate in the map in meters
    #   3) Angle in radians that the robot assumes once at X,Y

    DeskA_location = [-1.178, 0.996, -3.001]
    DeskB_location = [-8.370, 1.338, 0.276]

    B_x, B_y, B_yaw = DeskB_location
    A_x, A_y, A_yaw = DeskA_location

    RealTimesetGoal = realtimeController()
    result = RealTimesetGoal.publishMoveBase(A_x, A_y, A_yaw)
    #result = RealTimesetGoal.publishMoveBase(B_x, B_y, B_yaw)

    if result == True:
        rospy.loginfo("Error")
    else:
        rospy.loginfo("Goal reached successfully")




if __name__ == '__main__':

    # initialize ros node
    rospy.init_node('navigate_robot_node', anonymous=False)
    # define a subscriber to retrive tracked bodies
    #rospy.Subscriber('/pose_gesture', PostureGesture, controller_callback)
    controller_callback()