import rclpy
from rclpy.node import Node

from my_chatter_msgs.msg import TimestampString


class PublisherUser(Node):
    def __init__(self):
        super().__init__('Publisher')
        self.publisher = self.create_publisher(
            TimestampString, '/user_messages', 10
        )

    def run(self):
        while rclpy.ok():
            text = input('Please enter a line of text and press <Enter>: ')
            send_time = self.get_clock().now().nanoseconds

            if not rclpy.ok():
                break

            msg = TimestampString()
            msg.msg = text
            msg.timestamp = send_time

            self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PublisherUser()

    try:
        node.run()
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
