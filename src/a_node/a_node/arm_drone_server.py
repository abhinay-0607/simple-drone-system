#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ArmDrone


class ArmDroneServer(Node):

    def __init__(self):
        super().__init__("arm_drone_server")

        self.arm_server = self.create_service(
            ArmDrone,
            "arm_drone",
            self.callback_arm_drone
        )

        self.get_logger().info("Arm Drone Server has been started")

    def callback_arm_drone(
        self,
        request: ArmDrone.Request,
        response: ArmDrone.Response
    ):

        if request.arm:
            self.get_logger().info("Drone Armed")
            response.success = True
            response.message = "Drone armed successfully"
        else:
            self.get_logger().info("Drone Disarmed")
            response.success = True
            response.message = "Drone disarmed successfully"

        return response


def main(args=None):
    rclpy.init(args=args)

    node = ArmDroneServer()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()