
from redis import Redis as _Redis

from pickle import dumps, loads
from redis.client import Pipeline as _Pipeline

def is_int(num):
    return num.lstrip("+-").strip("0123456789").strip() == ""
def is_float(num):
    return num.lstrip("+-").strip("0123456789.").strip() == ""


REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,
}

### Cache处理
class Redis(_Redis):
    # 本身为主,负责写,slave为从,负责读
    slave = _Redis(**REDIS)
    dump_flag = b'ed32980f05054ca4b680e9656d6ea661'
    read_operator = [
        'GET', 'HGET', 'HMGET',
        'HEXISTS', 'KEYS', 'HLEN','HKEYS',
        'HGETALL', 'HVALS', 'HSTRLEN',
        'PUBLISH', 'PUBSUB CHANNELS', 'PUBSUB NUMPAT', 'PUBSUB NUMSUB',
    ]

    def pickle_data(self, data):
        '''将数据序列化为二进制'''
        if isinstance(data, bool):
            return self.dump_flag + dumps(data)
        if isinstance(data, (int, str, float, bytes)):
            return data

        return self.dump_flag + dumps(data)

    def unpickle_data(self, data):
        '''将数据反序列化为对象'''
        if isinstance(data, (int, float)):
            return data
        if isinstance(data, bytes) and data.startswith(self.dump_flag):
            data = data.replace(self.dump_flag, b'')
            return loads(data)

        if isinstance(data, dict):
            return {self.unpickle_data(key): self.unpickle_data(value) for key, value in data.items()}

        if isinstance(data, (tuple, list)):
            return [self.unpickle_data(item) for item in data]

        data=data.decode()
        if is_int(data):
            return int(data)
        if is_float(data):
            return float(data)
        return data

    def execute_command(self, *args, **options):
        '''执行命令'''
        # 针对keys()操作
        if '*' in args:
            return super().execute_command(*args, **options)

        # 针对一般的操作,将数据序列化为二进制
        args_list = [self.pickle_data(item) for item in args]
        return super().execute_command(*args_list, **options)

    def parse_response(self, connection, command_name, **options):
        # 针对read_operator里的读操作,将结果反序列化为对象
        if command_name in self.read_operator:
            result = self.slave.parse_response(connection, command_name, **options)
            return self.unpickle_data(result)

        # 针对一般的操作
        result = super().parse_response(connection, command_name, **options)
        return result

    def pipeline(self, transaction=True, shard_hint=None):
        return Pipeline(
            self.connection_pool,
            self.response_callbacks,
            transaction,
            shard_hint)

class Pipeline(Redis,_Pipeline):

    # execute = self._execute_transaction
    def _execute_transaction(self, connection, commands, raise_on_error):
        '''处理事务的函数'''
        data=super()._execute_transaction(connection, commands, raise_on_error)
        return self.unpickle_data(data)

rds=Redis(**REDIS)
