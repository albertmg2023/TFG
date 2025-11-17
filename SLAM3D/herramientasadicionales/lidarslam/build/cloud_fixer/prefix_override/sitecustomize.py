import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/miningdox/tfg/pruebas/herramientasadicionales/lidarslam/install/cloud_fixer'
