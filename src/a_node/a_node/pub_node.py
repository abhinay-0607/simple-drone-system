#!usr/bin/env/python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class PublishNode(Node):
    def __init__(self):
        super().__init__('DroneAltitudePublisher')
        self.get_logger().info("DroneAltitudePublisher has been started")
        self.number=10
        self.number_publisher=self.create_publisher(Int64,"number",10)
        self.num_adder=self.create_timer(1.0,self.number_adder)
        self.number_timer_=self.create_timer(1.0,self.publish_number)
    def publish_number(self):
        msg=Int64()
        msg.data=self.number
        self.number_publisher.publish(msg)
    def number_adder(self):
        self.number=self.number+1    

        
def main(args=None):
    rclpy.init(args=args)
    node = PublishNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()