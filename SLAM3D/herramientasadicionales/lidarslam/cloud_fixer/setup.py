from setuptools import setup

package_name = 'cloud_fixer'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Tu Nombre',
    maintainer_email='tu@email.com',
    description='Nodo para arreglar nubes LIDAR sin intensidad',
    license='MIT',
    entry_points={
        'console_scripts': [
            'cloud_fixer_node = cloud_fixer.cloud_fixer_node:main',
        ],
    },
)

