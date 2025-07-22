_registry = {}

def register(name: str):
    def decorator(fn):
        _registry[name] = fn
        return fn
    return decorator


def get(name: str):
    return _registry[name]


def formats():
    return list(_registry.keys())

