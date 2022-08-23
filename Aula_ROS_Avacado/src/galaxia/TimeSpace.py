#!/usr/bin/env python3

import rospy
import tf
import tf2_ros
import math
import geometry_msgs.msg
import sys

class Sistema:
    def __init__(self, referencial, objeto, raio, x):
        print(type(referencial), type(objeto), type(raio), type(x))
        self.referencial = referencial
        self.objeto = objeto
        self.raio = raio
        self.angulo = x
        self.rate = rospy.Rate(100)
        self.br = tf2_ros.TransformBroadcaster()
        self.t = geometry_msgs.msg.TransformStamped()
        self.Girar()

    def Girar(self):
        self.t.header.stamp = rospy.Time.now()
        self.t.header.frame_id = self.referencial
        self.t.child_frame_id =  self.objeto
        self.t.transform.translation.x = self.raio * math.sin(self.angulo)
        self.t.transform.translation.y = self.raio * math.cos(self.angulo)
        self.t.transform.translation.z = 0.0
        self.t.transform.rotation.x = 0
        self.t.transform.rotation.y = 0
        self.t.transform.rotation.z = 0
        self.t.transform.rotation.w = 1
        self.br.sendTransform(self.t)
        self.rate.sleep()
        

        
            
if __name__ == '__main__':
    rospy.init_node('star_position', anonymous=True)
    sistema = rospy.get_param('/sistema')

    while not rospy.is_shutdown():
        tempo_terrestres = rospy.Time.now().to_sec()
        for entidade in sistema:
            if sistema[entidade].get('referencia')!= None: 
                Sistema(
                    str(sistema[entidade].get('referencia')), 
                    str(sistema[entidade].get('id')), 
                    sistema[entidade].get('raio'), 
                    sistema[entidade].get('velocidade') * tempo_terrestres
                    )
                
    
    



