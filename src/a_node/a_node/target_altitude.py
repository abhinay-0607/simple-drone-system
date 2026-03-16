#!/usr/bin/env/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class TargetAltitudeNode(Node):
    def __init__(self):
        super().__init__("TargetAltitude")
        self.counter=0
        self.create_subscription(Int64,"number",self.callback,10)
        self.get_logger().info("TargetAltitude has been started")
    def callback(self,msg:Int64):
        self.counter=self.counter+msg.data
        self.get_logger().info("TargetAltitude " +str(self.counter))

def main(args=None):
    rclpy.init(args=args)
    node = TargetAltitudeNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()      
