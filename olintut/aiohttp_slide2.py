import asyncio

from concurrent.futures import ThreadPoolExecutor
from aiohttp import web

from .magic_slide1 import long_running_magic_number_generator

MAGIC_THREAD_POOL = ThreadPoolExecutor(5)

@asyncio.coroutine
def magic_handler(request):
    # if using async def, `yield from` becomes `await`
    magic_number = yield from request.loop.run_in_executor(
        MAGIC_THREAD_POOL, long_running_magic_number_generator
    )
    return web.Response(status=200, text=str(magic_number))


async def boring_handler(request):
    return web.Response(status=200, text="yikes")


def main(port):
    app = web.Application()
    app.add_routes([
        web.get("/magic", magic_handler),
        web.get("/boring", boring_handler),
    ])

    web.run_app(
        app,
        host="0.0.0.0",
        port=port
    )


if __name__ == "__main__":
    main(port=5000)
