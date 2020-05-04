from message import Message


class MessageManager:
    def __init__(self, input_vector_size, topic_name):
        self.input_vector_size = input_vector_size
        self.topic_name = topic_name
        self.messages_sent = 0
        self.message = Message()
        
    def has_reached_input_size_limit(self):
        return len(self.message.x) >= self.input_vector_size
    
    def reset_message(self):
        self.message = Message()

    def increment_message_sent(self):
        self.messages_sent += 1
        self.message.id = self.messages_sent
