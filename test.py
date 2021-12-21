import asyncio
from threading import Timer

async def hello_world():
    await asyncio.sleep(1)
    print('Hello World!')
    Timer(3, wait).start()

def wait():
    asyncio.run(hello_world())

wait()