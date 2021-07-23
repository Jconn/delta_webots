import rclpy
from webots_ros2_core.webots_node import WebotsNode
import time


class DeltaWebotsDriver(WebotsNode):
    def __init__(self, args):
        self.init_time = time.monotonic()
        super().__init__(name='delta_robot', args=args)
        self.motors = [
            self.robot.getDevice('delta_arm_0_motor'),
            self.robot.getDevice('delta_arm_1_motor'),
            self.robot.getDevice('delta_arm_2_motor')
        ]
        self.encoders = [
            self.robot.getDevice('delta_arm_0_encoder'),
            self.robot.getDevice('delta_arm_1_encoder'),
            self.robot.getDevice('delta_arm_2_encoder')
        ]
        self.routine = [(0., 0., 0.), (1.2, 1.0, -.3),
                        (-.20, -.25, 1.0), (-.40, -.7, -.7)]
        self.routine_idx = 0
        self.routine_time = 0

    def step(self, ms):
        super().step(ms)
        self.routine_time += ms
        if self.routine_time > 1500:
            self.move_delta(self.routine[self.routine_idx])
            self.routine_idx += 1
            self.routine_idx %= len(self.routine)
            self.routine_time = 0

    def move_delta(self, motor_positions):
        for idx, target_angle in enumerate(motor_positions):
            self.motors[idx].setPosition(target_angle)


def main(args=None):
    rclpy.init(args=args)
    my_webots_driver = DeltaWebotsDriver(args=args)
    rclpy.spin(my_webots_driver)
    my_webots_driver.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
