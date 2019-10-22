import asyncio


class Application:
    def __init__(self):

        self.components = []

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
