#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

def subscriber(data):
    rospy.loginfo(rospy.get_caller_id() + "I recieved -- %s", data.data)

def listener():
    rospy.init_node('subscriberNode', anonymous=True)
    rospy.Subscriber("talker", String, subscriber)
    rospy.spin()


if __name__ == '__main__':
        listener()