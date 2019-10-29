from peewee import *
import peewee
import logging
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = SqliteDatabase('yqmiot.db')

class BaseModel(Model):
    class Meta:
        database = db

class Device(BaseModel):
    did = PrimaryKeyField() # 设备id
    name = CharField() # 名称
    model = CharField() # 设备型号
    owner = IntegerField() # 所有者
    token = CharField() # 密码
    create_time = DateField() # 创建时间

class User(BaseModel):
    uid = PrimaryKeyField()
    username = CharField() # 用户名，符合一定规则
    nickname = CharField() # 用来展示的
    password = CharField()
    email = CharField()
    create_time = DateField() # 创建时间

class Config(BaseModel):
    id = PrimaryKeyField()
    key = CharField()
    value = CharField()

if __name__ == "__main__":
    # db.create_tables([Device, User, Config])
    # print(DeviceDoesNotExist)
    try:
        x = Device.get(Device.did==1000)
    except Device.DoesNotExist:
        print("没找到")
