# -*- encoding: utf-8 -*-
import json


class Packet:
    __slots__ = ('mid', 'dst', 'src', 'cmd', 'data')

    def __init__(self):
        self.mid = None  # int
        self.cmd = None  # str
        self.dst = None  # int
        self.src = None  # int
        self.data = None  # json

    def to_json(self):
        return json.dumps({
            "mid": self.mid,
            "dst": self.dst,
            "src": self.src,
            "cmd": self.cmd,
            "data": self.data
        })

    def from_json(self, str):
        data = json.loads(str)
        # self.mid = int(data.get("mid"))
        self.dst = int(data.get("dst"))
        self.src = int(data.get("src"))
        self.cmd = data.get("cmd")
        self.data = data.get("data")

    def __repr__(self):
        return "<Packet> cmd: {}, dst: {}, src: {}".format(self.cmd, self.dst, self.src)
