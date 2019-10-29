import asyncio
import datetime

from model import Device

app = None

# 不知道什么设计，就暂时这么定了

NODE_STATE_OFFLINE = 0
NODE_STATE_ONLINE = 1


class Node:
    def __init__(self):
        self.did = None
        self.name = None
        self.model = None
        self.state = NODE_STATE_OFFLINE


class Application:
    def __init__(self):
        global app
        app = self

        self.components = []
        self.nodes = {}  # did => node

    async def setup(self):
        print("application setup ...")
        for c in self.components:
            await c.setup()

    async def run(self):
        print("application run ...")
        for c in self.components:
            await c.run()

    def get_loop(self):
        return self.loop

    def regist_component(self, comp):
        if not comp:
            return
        if comp in self.components:
            return
        self.components.append(comp)

    def get_node(self, did, load: bool = False):
        if did not in self.nodes:
            # TODO 查询数据库
            try:
                m = Device.get(Device.did == did)
            except Device.DoesNotExist:
                # XXX 不存在直接创建
                m = Device.create(did=did, name=str(
                    did), model="null", owner=0, token="admin", create_time=datetime.date(2012, 12, 21))
            node = Node()
            node.did = m.did
            node.name = m.name
            node.state = NODE_STATE_OFFLINE
            self.nodes[did] = node
            return node 
        return self.nodes.get(did)