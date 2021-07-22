from setuptools import setup
import os

package_name = 'delta_webots'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name,
                      'worlds'), [os.path.join('worlds', 'test_world.wbt')]),
        (f'share/{package_name}/launch', ['launch/delta.launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='johnconn',
    maintainer_email='johnconn@umich.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driver = delta_webots.driver:main'
        ],
    },
)
