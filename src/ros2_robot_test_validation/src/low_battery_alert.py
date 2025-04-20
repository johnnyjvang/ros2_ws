# File: low_battery_alert.py'
# chmod +x low_battery_alert.py
# ros2 run ros2_robot_test_validation low_battery_alert

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState

class BatteryMonitor(Node):
    def __init__(self):
        super().__init__('battery_monitor')
        self.subscription = self.create_subscription(
            BatteryState,
            '/battery_state',  # <- Check your topic name
            self.battery_callback,
            10
        )
        self.low_voltage_threshold = 10.5  # Volts for 3S LiPo (safe zone)

    def battery_callback(self, msg):
        voltage = msg.voltage
        if voltage < self.low_voltage_threshold:
            self.get_logger().warn(f'🚨 LOW BATTERY WARNING: {voltage:.2f}V! 🚨')
            print('\a')  # Beep in terminal (if your system supports it)

def main(args=None):
    rclpy.init(args=args)
    battery_monitor = BatteryMonitor()
    rclpy.spin(battery_monitor)
    battery_monitor.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
