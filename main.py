import os
import sys
import time

import sqlite3
import jinja2
import peewee
import aiohttp

async def index(request):
    return aiohttp.web.Response(text=u"")

app = aiohttp.web.Application()