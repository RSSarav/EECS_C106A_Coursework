import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException

from my_chatter_msgs.msg import TimestampString


class SubscriberUser(Node):
    def __init__(self):
        super().__init__('Subscriber')
        self.subscription = self.create_subscription(
            TimestampString,
            '/user_messages',
            self.receive_message,
            10,
        )

    def receive_message(self, msg):
        received_time = self.get_clock().now().nanoseconds

        print(
            f'Message: {msg.msg}, '
            f'Sent at: {msg.timestamp}, '
            f'Received at: {received_time}',
            flush=True,
        )


def main(args=None):
    rclpy.init(args=args)
    node = SubscriberUser()

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
