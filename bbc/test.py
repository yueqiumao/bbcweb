# -*- encoding: utf-8 -*-
import asyncio

from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2


async def main():
    client = MQTTClient()
    await client.connect("mqtt://mikuq.com:21883")
    print("connected")
    import time
    time.sleep(10)
    await client.subscribe([("bbc", QOS_0)])
    print("sub ok")

    while True:
        time.sleep(1)
        await client.publish("bbc", "葱头在不在？".encode("utf8"))
        print("ok")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
