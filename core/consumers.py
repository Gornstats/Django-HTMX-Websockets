from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        # print(self.channel_name) - gives unique name of client consumer
        self.GROUP_NAME = 'user-notifications' #fixed group for testing that all users are added to
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )       
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )
    
    def user_joined(self, event):
        self.send(text_data=event['text'])
