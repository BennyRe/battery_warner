#!/usr/bin/env python
import roslib; roslib.load_manifest('battery_warner')
import rospy
from p2os_driver.msg import BatteryState

warningVoltage = 11.49

def callback(battery_state):
    if battery_state.voltage <= warningVoltage:
        rospy.logwarn('battery voltage below %fV!!!!', warningVoltage)

def listener():
    rospy.init_node('battery_Warner', anonymous=True)
    rospy.Subscriber("battery_state", BatteryState, callback)
    rospy.loginfo('Battery warner started. It will warn you below an voltage of %fV', warningVoltage)
    rospy.spin()

if __name__ == '__main__':
    listener()