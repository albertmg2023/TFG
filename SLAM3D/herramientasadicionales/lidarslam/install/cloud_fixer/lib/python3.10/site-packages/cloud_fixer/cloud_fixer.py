#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs_py.point_cloud2 as pc2
import std_msgs.msg

class CloudFixer(Node):
    def __init__(self):
        super().__init__('cloud_fixer')
        self.sub = self.create_subscription(PointCloud2, '/webots/lidar', self.callback, 10)
        self.pub = self.create_publisher(PointCloud2, '/webots/lidar_with_intensity', 10)

    def callback(self, msg):
        points = list(pc2.read_points(msg, field_names=["x", "y", "z"], skip_nans=True))
        fixed_points = [(x, y, z, 1.0) for x, y, z in points]

        fields = [
            PointField('x', 0, PointField.FLOAT32, 1),
            PointField('y', 4, PointField.FLOAT32, 1),
            PointField('z', 8, PointField.FLOAT32, 1),
            PointField('intensity', 12, PointField.FLOAT32, 1),
        ]

        header = std_msgs.msg.Header()
        header.stamp = msg.header.stamp
        header.frame_id = msg.header.frame_id

        cloud_out = pc2.create_cloud(header, fields, fixed_points)
        self.pub.publish(cloud_out)

rclpy.init()
node = CloudFixer()
rclpy.spin(node)
