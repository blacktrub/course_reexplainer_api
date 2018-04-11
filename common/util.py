import re

import redis


class RedisDict:

    def __init__(self, **redis_kwargs):
        self.__db = redis.Redis(**redis_kwargs)

    def __len__(self):
        return self.__db.keys().__len__()

    def __setitem__(self, key, value):
        self.__db.set(key, value)

    def __getitem__(self, key):
        return self.__db.get(key).decode()

    def __contains__(self, item):
        return True if self[item] else False

    def __iter__(self):
        for key in self.__db.keys():
            yield key.decode()

    def expire(self, key, time):
        self.__db.expire(key, time)

    def pop(self, key):
        return self.__db.delete(key)


class ReExplain:

    def __init__(self, expression):
        self.expression = expression

    def __call__(self):
        pass
