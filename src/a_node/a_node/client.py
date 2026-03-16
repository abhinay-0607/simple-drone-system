#!/usr/bin/env/python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ResetTargetAltitude

class client(Node):
    def __init__(self):
        super().__init__("client")
        self.client = self.create_client(ResetTargetAltitude,"resettargetaltitude")
    def call_reset_counter(self,value):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("waiting for service arm_drone_server")
        request = ResetTargetAltitude.Request()
        request.reset_value = value
        future = self.client.call_async(request)
        future.add_done_callback(self.callback_reset_counter)
    def callback_reset_counter(self,future):     
        response = future.result()
        self.get_logger().info("Response from server: " + str(response.success) + " " + str(response.message))
def main(args=None):
    rclpy.init(args=args)
    node = client()
    node.call_reset_counter(20)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main() 


