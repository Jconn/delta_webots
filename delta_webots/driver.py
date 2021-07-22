import rclpy
from webots_ros2_core.webots_node import WebotsNode
import time
import pdb


class DeltaWebotsDriver(WebotsNode):
    def __init__(self, args):
        self.init_time = time.monotonic()
        super().__init__(name='delta_robot', args=args)
        # Calling start_device_manager automatically inserts Webots devices
        # from Gazebo devices and creates ROS2 topics for them.
        # It receives a dict with params that allow to configure the device
        # behavior.
        # Refer to SensorDevice in webots_ros2_core for all the parameters
        # that can be passed.
        # self.start_device_manager({
        #     'imu accelerometer+imu gyro': {
        #         'topic_name': '/imu/data_raw',
        #     },
        #     'front-realsense-435-color': {
        #         'topic_name': '/front/camera/color',
        #         'frame_id': 'front_camera_color_frame'
        #     },
        #     'front-realsense-d435-depth': {
        #         'topic_name': '/front/camera/depth',
        #         'frame_id': 'front_camera_depth_frame'
        #     },
        #     'delta-realsense-435-color': {
        #         'topic_name': '/delta/camera/color',
        #         'frame_id': 'delta_camera_color_frame'
        #     },
        #     'delta-realsense-d435-depth': {
        #         'topic_name': '/delta/camera/depth',
        #         'frame_id': 'delta_camera_depth_frame'
        #     },
        #     'radar_0_ray': {
        #         'topic_name': '/radar/node0',
        #         'frame_id': 'radar_0_sim_base_link'
        #     },
        #     'radar_3_ray': {
        #         'topic_name': '/radar/node3',
        #         'frame_id': 'radar_3_sim_base_link'
        #     },
        #     'radar_4_ray': {
        #         'topic_name': '/radar/node4',
        #         'frame_id': 'radar_4_sim_base_link'
        #     },
        #     'gps gps': {
        #         'topic_name': '/gps/data',
        #         'frame_id': 'gps_base_link'
        #     }
        # })

    def step(self, ms):
        super().step(ms)
        max_setpoint = -.45
        e1 = self.robot.getDevice('delta_arm_0_encoder')
        setpoint = e1.getValue() - .0304

        if max_setpoint > setpoint:
            setpoint = max_setpoint
            self.get_logger().info('capping')

        d1 = self.robot.getDevice('delta_arm_0_motor')
        d1.setPosition(setpoint)
        e1 = self.robot.getDevice('delta_arm_0_encoder')

        d2 = self.robot.getDevice('delta_arm_1_motor')
        d2.setPosition(setpoint)
        e2 = self.robot.getDevice('delta_arm_1_encoder')

        d3 = self.robot.getDevice('delta_arm_2_motor')
        d3.setPosition(setpoint)
        e3 = self.robot.getDevice('delta_arm_2_encoder')
        self.get_logger().info(
            f'{e1.getValue()}, {e2.getValue()}, {e3.getValue()}')


def main(args=None):
    rclpy.init(args=args)
    my_webots_driver = DeltaWebotsDriver(args=args)
    rclpy.spin(my_webots_driver)
    my_webots_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
