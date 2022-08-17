#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
import math

class ModularVelocidade():
    def __init__(self):

        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('velocidade', Twist, self.callback)

        self.modulo_angular = rospy.Publisher('modulo_angular', Float64, queue_size=10)
        self.modulo_linear = rospy.Publisher('modulo_linear', Float64, queue_size=10)

    def callback(self, velocidade):

        linear_x, linear_y, linear_z = velocidade.linear.x, velocidade.linear.y, velocidade.linear.z
        modulo_linear = Float64()
        modulo_linear.data = math.sqrt(linear_x**2 + linear_y**2 + linear_z**2)

        angular_x, angular_y, angular_z = velocidade.angular.x, velocidade.angular.y, velocidade.angular.z
        modulo_angular = Float64()
        modulo_angular.data = math.sqrt(angular_x**2 + angular_y**2 + angular_z**2)
        
        rospy.loginfo('Modulo Linear')
        rospy.loginfo(modulo_linear)

        rospy.loginfo('Modulo Angular')
        rospy.loginfo(modulo_angular)
        
        self.modulo_linear.publish(modulo_linear)
        self.modulo_angular.publish(modulo_angular)
        


if __name__ == '__main__':
    l = ModularVelocidade()
    rospy.spin()