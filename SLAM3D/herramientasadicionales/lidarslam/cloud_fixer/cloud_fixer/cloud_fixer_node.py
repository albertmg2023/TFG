#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs_py.point_cloud2 as pc2
import std_msgs.msg

class CloudFixer(Node):
    def __init__(self):
        super().__init__('cloud_fixer')
        self.sub = self.create_subscription(PointCloud2, '/rbwatcher/rbwatcher/rbwatcher/top_3d_laser/point_cloud', self.callback, 10)
        self.pub = self.create_publisher(PointCloud2, '/rbwatcher/rbwatcher/rbwatcher/top_3d_laser/point_cloud_intensity', 10)

    def callback(self, msg):
        points = list(pc2.read_points(msg, field_names=["x", "y", "z"], skip_nans=True))
        fixed_points = [(x, y, z, 1.0) for x, y, z in points]

        fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
            PointField(name='intensity', offset=12, datatype=PointField.FLOAT32, count=1),
        ]

        header = std_msgs.msg.Header()
        header.stamp = msg.header.stamp
        header.frame_id = msg.header.frame_id

        cloud_out = pc2.create_cloud(header, fields, fixed_points)
        self.pub.publish(cloud_out)

rclpy.init()
node = CloudFixer()
rclpy.spin(node)

