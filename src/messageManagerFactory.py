from messageManager import MessageManager
from message import Message


class MessageManagerFactory:
    def __init__(self):
        self.message_managers = []

    def create(self, max_input_size, topic_name):
        """
        Adds a message manager object that will handle the streaming for a given topic.
        :param max_input_size: Size of the array that will be streamed
        :param topic_name: Name of the topic to which the data will ben sent
        """
        message_manager = MessageManager(max_input_size, topic_name)
        self.message_managers.append(message_manager)

    def get_all(self):
        return self.message_managers

    def add_input(self, x):
        """
        Adds an element to every message manager currently defined.
        :param x: Element to be added
        """
        for message_manager in self.message_managers:
            message_manager.message.x.append(x)
