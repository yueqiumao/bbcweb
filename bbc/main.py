import os
import sys
import time
import asyncio

import sqlite3
import jinja2
import peewee


async def main_async():
    print("BBC start ...")

    import application

    app = application.Application()

    import mqttconnection
    mc = mqttconnection.MqttConnection()
    app.regist_component(mc)

    import httpconnection
    hc = httpconnection.HttpConnection()
    app.regist_component(hc)

    await app.setup()
    await app.run()

    print("BBC running ...")


def main():
    loop = asyncio.get_event_loop()
    loop.create_task(main_async())
    loop.run_forever()


if __name__ == "__main__":
    main()
