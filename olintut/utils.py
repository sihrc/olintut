import uuid

from decorator import decorator

@decorator
def logger(f, *args, **kwargs):
    try:
        func_id = uuid.uuid1().hex[:5]
        print(f"{f.__name__}:{func_id} started.")
        return f(*args, **kwargs)
    except:
        print(f"{f.__name__}:{func_id} failed gloriously.")
    finally:
        print(f"{f.__name__}:{func_id} complete.")
