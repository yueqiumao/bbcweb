import os
import sys
import time

import sqlite3
import jinja2
import peewee
import aiohttp.web

# async def index(request):
#     return aiohttp.web.Response(text=u"这里是大球的小破车，大球的小破车将来可是要上天的")

# app = aiohttp.web.Application()
# app.add_routes([
#     aiohttp.web.get("/", index)
# ])
# aiohttp.web.run_app(app)

def main():
    import application

    app = application.Application()
    app.setup()
    app.run()

if __name__ == "__main__":
    main()