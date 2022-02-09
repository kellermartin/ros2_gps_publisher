import rclpy
import serial
import io
import pynmea2 as nmea

from sensor_msgs.msg import NavSatFix

def main(args=None):
    rclpy.init(args=args)
    
    ser = serial.Serial('/dev/ttyACM0', 4800, timeout=5.0)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))   

    node = rclpy.create_node('gps_publisher')
    publisher = node.create_publisher(NavSatFix, 'NavSatFix', 10)

    def gpstimer_callback():
        try:
            line = sio.readline()
            if "$GPGGA" in line:
                msg = nmea.parse(line)
                print(repr(msg))
                # create navsat msg
                gps_msg = NavSatFix()
                gps_msg.altitude = float(msg.altitude)
                gps_msg.latitude = float(msg.latitude)
                gps_msg.longitude = float(msg.longitude)
                #node.get_logger().info('Publishing gps data - Altitude: "%s" Latitude: "%s" Longitude: "%s" '%msg.altitude, msg.lat, msg.lon)
                publisher.publish(gps_msg)     
        except nmea.ParseError as e:
            node.get_logger().warning('Parse error NMEA string')
        except serial.SerialException as e:
            node.get_logger().error('SerialException')    
            
        

    timer_period = 0.5  # seconds
    timer = node.create_timer(timer_period, gpstimer_callback)

    rclpy.spin(node)

    # Destroy the timer attached to the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_timer(timer)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
