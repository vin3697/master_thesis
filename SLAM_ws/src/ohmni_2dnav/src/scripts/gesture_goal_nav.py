#!/usr/bin/env python


import rospy
import geometry_msgs.msg
from ohmni_2dnav.msg import PostureGesture
from actionlib_msgs.msg import GoalStatus
import actionlib
from   move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import tf


obeyHuman = False
LocationA = True
LocationB = True

def publishMoveBase(l_x, l_y,l_yaw):
    #function take the co-ordinates and Action Cilent based move_base node executes to reach Goal!
    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = "map"     
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = l_x 
    goal.target_pose.pose.position.y = l_y

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
        return goal_client.get_result() # if "false" the goal is reached
    #rospy.loginfo("The location is : %d %d %d", l_x, l_y, l_yaw)
    #return False


def controller_callback(pose_gesture):
    #   1) X coordinate in the map in meters
    #   2) Y coordinate in the map in meters
    #   3) Angle in radians that the robot assumes once at X,Y

    #TODO: give proper Desk A and Desk B locations
    #initial location is the pose given in the AMCL launch file as parameter
    
    initial_location = [-1.178, 0.996, -3.001] #Marked A on floor
    DeskA_location = [-3.950, 1.390, -3.085]
    DeskB_location = [-6.030, 1.489, -3.029]
    #DeskB_location = [-8.370, 1.338, 0.276] #Marked B on floor


    B_x, B_y, B_yaw          = DeskB_location
    A_x, A_y, A_yaw          = DeskA_location
    init_x, init_x, init_yaw = initial_location 

    global obeyHuman

    personID       = pose_gesture.person_id
    person_pose    = pose_gesture.pose
    person_facing  = pose_gesture.facing
    person_gesture = pose_gesture.gesture

    if person_gesture == 'ObeyHuman':       #both hands near your chest
        obeyHuman = True
        rospy.loginfo("Obey Huaman")

    if person_gesture == 'DisobeyHuman':    #both hands away from chest
        obeyHuman = False
        rospy.loginfo("Disobey Human")

    #rospy.loginfo(obeyHuman)

    if ((obeyHuman) and (person_facing == 'FacingTowards') and (person_pose =='Standing')):

        global LocationA
        global LocationB
        #rospy.loginfo("%s", person_gesture)
        #rospy.loginfo("%s", person_facing)
        #rospy.loginfo("%s", person_pose)
        if (person_gesture == 'DeskA') and LocationA:                 #raise your one hand

            result = publishMoveBase(A_x, A_y, A_yaw)
            rospy.loginfo("Goal given by person %d",personID)
            if result == True:
                rospy.loginfo("Error: Goal not reached, going back to initial position")
                publishMoveBase(init_x, init_x, init_yaw) #Go back to the initial position if failed
            else:
                rospy.loginfo("Goal A reached successfully")
                LocationA = False
                LocationB = True

        if (person_gesture == 'DeskB') and LocationB:                 #raise your both hands
            result = publishMoveBase(B_x, B_y, B_yaw)
            rospy.loginfo("Goal given by person %d",personID)
            if result == True:
                rospy.loginfo("Error: Goal not reached, going back to initial position")
                publishMoveBase(init_x, init_x, init_yaw) 
            else:
                rospy.loginfo("Goal B reached successfully")
                LocationA = True
                LocationB = False
            


if __name__ == '__main__':

    # initialize ros node
    rospy.init_node('navigate_robot_node', anonymous=False)
    # define a subscriber
    rospy.Subscriber('/pose_gesture', PostureGesture, controller_callback)
    rospy.spin()
