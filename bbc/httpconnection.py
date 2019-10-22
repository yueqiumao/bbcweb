# -*- encoding: utf-8 -*-
import aiohttp.web
import asyncio


class HttpConnection:
    async def setup(self):
        print("http connection setup ...")

        self.app = aiohttp.web.Application()
        self.app.add_routes([
            aiohttp.web.get("/", self.index)
        ])

    async def run(self):
        print("http connection run ...")

        loop = asyncio.get_event_loop()
        self.srv = await loop.create_server(self.app.make_handler(), "0.0.0.0", 8000)

    async def index(self, request):
        return aiohttp.web.Response(text=u"这里是大球的小破车，大球的小破车将来可是要上天的")
