import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.error_sum = 0.0
        self.last_error = 0.0

    def update(self, error, dt):
        self.error_sum += error * dt
        derivative = (error - self.last_error) / dt
        output = self.kp * error + self.ki * self.error_sum + self.kd * derivative
        self.last_error = error
        return output

def scan_callback(scan):
    ranges = scan.ranges
    min_distance = min(ranges)
    error = 1 - min_distance
    control = pid_controller.update(error, scan.scan_time)
    twist = Twist()
    twist.linear.x = control
    drone_velocity_publisher.publish(twist)

if __name__ == '__main__':
    rospy.init_node('drone_controller')

    pid_controller = PIDController(0.5, 0.1, 0.2)
    drone_velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    laser_subscriber = rospy.Subscriber('/scan', LaserScan, scan_callback)

    rospy.spin()
