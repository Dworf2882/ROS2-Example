#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from drone_msgs.msg import Goal
import rclpy.qos

class DrawCircleNode(Node):
    i = 1
    point = []
    def __init__(self):
        super().__init__("draw_circle")
        self.pub = self.create_publisher(Goal,"/goal_pose",10)
        qos_profile = rclpy.qos.QoSProfile(depth=10)
        qos_profile.history = rclpy.qos.QoSHistoryPolicy.KEEP_LAST
        qos_profile.durability = rclpy.qos.QoSDurabilityPolicy.VOLATILE
        qos_profile.reliability = rclpy.qos.QoSReliabilityPolicy.BEST_EFFORT
        self.subSec = self.create_subscription(PoseStamped,"/point",self.points,qos_profile) 
        self.sub = self.create_subscription(PoseStamped, "/uav1/mavros/local_position/pose", self.sendVel, qos_profile)  
        self.get_logger().info("Start")
    def ab(self,a,b,pog):
        if abs(a-b) <= pog and abs(a-b) != 0:
            return True
        else:
            return False
    def points(self,msg):
        self.point.append((msg.pose.position.x,msg.pose.position.y,msg.pose.position.z))
    def sendVel(self,msg):
        mes = Goal()

        pose = msg.pose.position
        print("--------------------")
        print(self.i)
        print(pose.x)
        print(pose.y)
        print(pose.z)
        print(self.point)

        if len(self.point) == 0:
            pass
        elif len(self.point) == 1:
            mes.pose.point.x = self.point[0][0]
            mes.pose.point.y = self.point[0][1]
            mes.pose.point.z = self.point[0][2]
            self.pub.publish(mes)
        elif self.ab(pose.x,self.point[self.i-1][0],1) and self.ab(pose.y,self.point[self.i-1][1],1) and self.ab(pose.z,self.point[self.i-1][2],2):
            mes.pose.point.x = self.point[self.i][0]
            mes.pose.point.y = self.point[self.i][1]
            mes.pose.point.z = self.point[self.i][2]
            self.pub.publish(mes)
            self.get_logger().info("Goida")
            self.i += 1
            print(self.point[self.i-1][0])
            print(self.i)
def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()