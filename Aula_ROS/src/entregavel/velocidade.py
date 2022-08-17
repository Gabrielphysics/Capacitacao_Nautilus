#!/usr/bin/env python3

import rospy
import random
from geometry_msgs.msg import Twist

class Velocidade:
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        self.pub = rospy.Publisher('velocidade', Twist, queue_size=10)
        
    def start(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            velocidade = Twist()
            velocidade.linear.x = random.uniform(0, 30)
            velocidade.linear.y = random.uniform(0, 30)
            velocidade.linear.z = random.uniform(0, 30)
            
            velocidade.angular.x = random.uniform(0, 15)
            velocidade.angular.y = random.uniform(0, 15)
            velocidade.angular.z = random.uniform(0, 15)

            rospy.loginfo(velocidade)
            self.pub.publish(velocidade)
            rate.sleep()


if __name__ == '__main__':
    try:
        t = Velocidade()
        t.start()
    except rospy.ROSInterruptException:
        pass   