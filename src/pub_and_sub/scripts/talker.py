#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def publish():
    pub = rospy.Publisher('talker', String, queue_size=10)
    rospy.init_node('publish_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        publishString = "this is being published"
        rospy.loginfo("Data is being sent")
        pub.publish(publishString)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish()
    except rospy.ROSInterruptException:
        pass

