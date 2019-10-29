# -*- encoding: utf-8 -*-
import asyncio
import application

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2
from packet import Packet

MQTT_COMMAND_LOGIN = "login"
MQTT_COMMAND_LOGOUT = "logout"
MQTT_COMMAND_PING = "ping"


class MqttConnection:

    async def setup(self):
        print("mqtt connection setup ...")
        self.client = MQTTClient()
        await self.client.connect("mqtt://yqmiot.com")
        await self.client.subscribe([("yqmiot/0/#", QOS_0)])
        loop = asyncio.get_event_loop()
        loop.create_task(self.loop())

    async def run(self):
        print("mqtt connection run ...")

    async def loop(self):
        while True:

                msg = await self.client.deliver_message()
                pkt = msg.publish_packet
                topic = pkt.variable_header.topic_name
                payload = pkt.payload.data.decode("utf8")

                topics = topic.split("/")
                if len(topics) != 3:
                    print("MqttServer: invalid packet.0")
                    continue

                try:
                    packet = Packet()
                    packet.from_json(payload)

                    if packet.cmd not in (MQTT_COMMAND_LOGIN, MQTT_COMMAND_LOGOUT, MQTT_COMMAND_PING):
                        raise Exception()
                except e:
                    print("MqttServer: invalid packet.1")
                    continue

                try:
                    if topics[0] != "yqmiot" \
                            or int(topics[1]) != 0 \
                            or int(topics[2]) != int(packet.src):
                        print("MqttServer: invalid packet.2")
                        continue

                    self.handle_packet(packet)
                except:
                    raise
                    print("MqttServer: invalid packet.3")


    def handle_packet(self, packet):
        if packet.cmd == MQTT_COMMAND_LOGIN:
            self.on_login(packet)
        elif packet.cmd == MQTT_COMMAND_LOGOUT:
            self.on_logout(packet)
        elif packet.cmd == MQTT_COMMAND_PING:
            self.on_ping(packet)

    def on_login(self, packet):
        node = application.app.get_node(packet.src)
        print(node)

    def on_logout(self, packet):
        pass

    def on_ping(self, packet):
        pass