from peewee import *

import logging
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = SqliteDatabase('yqmiot.db')

class Device(Model):
    did = PrimaryKeyField() # 设备id
    name = CharField() # 名称
    model = CharField() # 设备型号
    owner = IntegerField() # 所有者
    token = CharField() # 密码
    create_time = DateField() # 创建时间

    class Meta:
        database = db

class User(Model):
    uid = PrimaryKeyField()
    username = CharField() # 用户名，符合一定规则
    nickname = CharField() # 用来展示的
    password = CharField()
    email = CharField()
    create_time = DateField() # 创建时间

    class Meta:
        database = db

if __name__ == "__main__":
    db.create_tables([Device, User])