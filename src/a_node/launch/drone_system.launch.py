from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    test_node = Node(
        package='a_node',
        executable='TestNode',
        name='test_node'
    )

    publisher_node = Node(
        package='a_node',
        executable='DroneAltitudePublisher',
        name='altitude_publisher'
    )

    target_node = Node(
        package='a_node',
        executable='TargetAltitude',
        name='target_altitude'
    )

    server_node = Node(
        package='a_node',
        executable='arm_drone_server',
        name='arm_drone_server'
    )

    client_node = Node(
        package='a_node',
        executable='arm_drone_client',   # updated here
        name='arm_drone_client'
    )

    return LaunchDescription([
        test_node,
        publisher_node,
        target_node,
        server_node,
        client_node
    ])