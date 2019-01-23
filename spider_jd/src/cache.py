import redis

class cache:
    def store_session(key='name', value=''):
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        return r.set(key, value)

    def get_session(key='name'):
        r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        return r.get(key)