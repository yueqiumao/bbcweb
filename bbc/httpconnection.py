# -*- encoding: utf-8 -*-
import aiohttp.web
import asyncio


class HttpConnection:
    async def setup(self):
        print("http connection setup ...")

    async def run(self):
        print("http connection run ...")


# async def index(request):
#     return aiohttp.web.Response(text=u"这里是大球的小破车，大球的小破车将来可是要上天的")

# app = aiohttp.web.Application()
# app.add_routes([
#     aiohttp.web.get("/", index)
# ])
# aiohttp.web.run_app(app)
