from diskcache import Cache

cache = Cache('/tmp/botcache')


def init_diskcache(path='/tmp/cache/'):
    global hash_cache
    hash_cache = Cache(path)
