def cache_deco(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)