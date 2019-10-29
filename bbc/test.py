# -*- encoding: utf-8 -*-
import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2


async def main():
    client = MQTTClient()
    await client.connect("mqtt://yqmiot.com")
    print("connected")

    await client.publish("yqmiot/0/10003", '{"src": 10003, "dst": 0, "cmd": "login", "data": null}'.encode("utf8"))
    print("ok")

    import sys
    sys.exit(0)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
