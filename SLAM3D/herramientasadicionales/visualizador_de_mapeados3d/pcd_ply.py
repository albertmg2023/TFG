import open3d as o3d

pcd = o3d.io.read_point_cloud("/home/miningdox/tfg/sLAMSRESULTS/lidarros/gazebo/map.pcd")
o3d.visualization.draw_geometries([pcd])
