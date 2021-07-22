# Built-in imports
from pathlib import Path

# External imports
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory

package_name = 'delta_webots'
world_filename = 'test_world.wbt'

world_path = Path(
    get_package_share_directory(package_name)) / 'worlds' / world_filename
launch_file_path = Path(get_package_share_directory(
    'webots_ros2_core')) / 'launch' / 'robot_launch.py'


def generate_launch_description():
    webots = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(str(launch_file_path)),

        # Look at the available arguments of this webots launch file here:
        # https://github.com/cyberbotics/webots_ros2/blob/master/webots_ros2_core/launch/robot_launch.py
        launch_arguments=[
            ('package', package_name),
            ('executable', 'driver'),
            ('world', str(world_path)),
        ])

    return LaunchDescription([webots])
