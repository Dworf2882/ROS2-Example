import rclpy
from rclpy.node import Node
from drone_msgs.msg import Goal
class point(Node):
    i = 0
    points = [(0.0,0.0,5.0),(10.0,10.0,10.0),(17.0,10.0,10.0),(0.0,0.0,5.0),(0.0,0.0,0.0)]
    def __init__(self):
        super().__init__("test_node")
        qos_profile = rclpy.qos.QoSProfile(depth=10)
        qos_profile.history = rclpy.qos.QoSHistoryPolicy.KEEP_LAST
        qos_profile.durability = rclpy.qos.QoSDurabilityPolicy.VOLATILE
        qos_profile.reliability = rclpy.qos.QoSReliabilityPolicy.BEST_EFFORT
        self.pub = self.create_publisher(Goal,"/point",qos_profile)
        self.tm = self.create_timer(2,self.prob)

    def prob(self):
        if self.i < len(self.points):
            mes = Goal()
            mes.pose.po
            self.pub.publish(mes)
            self.get_logger().info("DSdas")



            self.i += 1
            



def main(args=None):
    rclpy.init(args=args)
    node = point()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()