from setuptools import find_packages, setup

package_name = 'a_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/drone_system.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sai-abhinay',
    maintainer_email='24ec01030@iitbbs.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "TestNode=a_node.test_node:main",
            "DroneAltitudePublisher=a_node.pub_node:main",
            "TargetAltitude=a_node.target_altitude:main",
            "arm_drone_server=a_node.arm_drone_server:main",
            "arm_drone_client=a_node.client:main"
        ],
    },
)
