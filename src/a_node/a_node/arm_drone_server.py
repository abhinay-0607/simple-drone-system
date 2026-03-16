#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from my_robot_interfaces.srv import ResetTargetAltitude
class arm_drone_server(Node):
    def __init__(self):
        super().__init__("arm_drone_server")
        self.counter=0
        self.number_subscriber = self.create_subscription(Int64,"number",self.callback)
        self.reset_server = self.create_service(ResetTargetAltitude,"reset_target_altitude",self.callback_reset_counter)
        self.get_logger().info("arm drone server has been started")

    def callback_reset_counter(self,request:ResetTargetAltitude.Request,response:ResetTargetAltitude.Response):
        self.counter=request.reset_value
        self.get_logger().info("Reset Target Altitude to"+ str(self.counter))
        response.success="True"
        response.message="Success"
        return response
    def callback(self,msg:Int64):
        self.counter=msg.data
        self.get_logger().info("TargetAltitude " +str(self.counter))

def main(args=None):
    rclpy.init(args=args)
    node = arm_drone_server()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main() 