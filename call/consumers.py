import json

from channels.generic.websocket import AsyncWebsocketConsumer


class VideoCallConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['room_name']
 
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )  
        
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )     
        
    async def receive(self, text_data):
        receive_dict = json.loads(text_data)
        action = receive_dict['type']
        
        if action == 'offer':
            await self.channel_layer.group_send(    
                self.room_group_name, {
                    'type' : 'offer',
                    'data' : receive_dict['data']
                }
            )

        if action == 'answer':
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type' : 'answer',
                    'data' : receive_dict['data']
                }
            )
            
        if action == 'ICE':
            await self.channel_layer.group_send(
                self.room_group_name, {
                    'type' : 'ICE',
                    'data' : receive_dict['data']
                }
            )       
        
    async def offer(self, event):
        await self.send(text_data=json.dumps(
                {
                    'type' : 'offer',
                    'data' : event['data']
                }
            )
        )

    async def answer(self, event):
        await self.send(text_data=json.dumps(
                {
                    'type' : 'answer',
                    'data' : event['data'],
                }
            )
        )  
                  
    async def ICE(self, event):
        await self.send(text_data=json.dumps(
                {
                    'type' : 'ICE',
                    'data' : event['data']
                }
            )
        )
            