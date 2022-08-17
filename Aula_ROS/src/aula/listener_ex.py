#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import Float32

class Listener():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('exemplo', Point, self.callback)
        self.pub = rospy.Publisher('result', Float32, queue_size=10)

    def callback(self, msg):
        x, y, z = msg.x, msg.y, msg.z
        total = x + y + z
        f = Float32()
        f.data = total
        rospy.loginfo(f)
        self.pub.publish(f)

if __name__ == '__main__':
    l = Listener()
    rospy.spin()