#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ArmDrone


class ArmDroneClient(Node):

    def __init__(self):
        super().__init__("arm_drone_client")
        self.client = self.create_client(ArmDrone, "arm_drone")

    def call_arm_drone(self, value):
        while not self.client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service arm_drone_server")

        request = ArmDrone.Request()
        request.arm = value

        future = self.client.call_async(request)
        future.add_done_callback(self.callback_arm_drone)

    def callback_arm_drone(self, future):
        response = future.result()
        self.get_logger().info(
            "Response from server: " + str(response.success) + " " + str(response.message)
        )


def main(args=None):
    rclpy.init(args=args)

    node = ArmDroneClient()
    node.call_arm_drone(True)

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()