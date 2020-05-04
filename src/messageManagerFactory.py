from messageManager import MessageManager
from message import Message


class MessageManagerFactory:
    def __init__(self):
        self.message_managers = []

    def create(self, max_input_size, topic_name):
        message_manager = MessageManager(max_input_size, topic_name)
        self.message_managers.append(message_manager)

    def get_all(self):
        return self.message_managers

    def add_input(self, x):
        for message_manager in self.message_managers:
            message_manager.message.x.append(x)
