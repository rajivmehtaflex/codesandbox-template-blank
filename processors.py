# import asyncio
# import os,sys
# sys.version
# import aiohttp
# from timer import timer
# from multiprocessing import Pool
# from concurrent.futures import ThreadPoolExecutor

# URL='https://httpbin.org/uuid'

# async def getdata(session,URL):
#     async with session.get(URL) as response:
#         responsefromserver = await response.json()
#         print(responsefromserver['uuid'])


# async def sample():
#     async with aiohttp.ClientSession() as s:
#         tasks=[getdata(s,URL) for _ in range(100)]
#         await asyncio.gather(*tasks)

# @timer(1,1)
# def funcproc():
#     asyncio.run(sample())

import finetuner
finetuner.login()

print(finetuner.get_token())