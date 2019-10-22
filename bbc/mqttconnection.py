# -*- encoding: utf-8 -*-
import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2


class MqttConnection:

    async def setup(self):
        print("mqtt connection setup ...")
        self.client = MQTTClient()
        await self.client.connect("mqtt://mikuq.com:21883")
        await self.client.subscribe([("yqmiot/0/#", QOS_0)])
        loop = asyncio.get_event_loop()
        loop.create_task(self.loop())

    async def run(self):
        print("mqtt connection run ...")

    async def loop(self):
        while True:
            msg = await self.client.deliver_message()
            packet = msg.publish_packet
            topic = packet.variable_header.topic_name
            payload = packet.payload.data.decode("utf8")
            print(topic, payload)
