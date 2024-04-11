import aiohttp
import asyncio
import json
import os
os.chdir(os.getcwd())
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.org/posts') as response:
            return await response.text()
y = json.loads(asyncio.run(main()))
for i in range(len(y)):
    os.mkdir(f"file{i+1}")
    with open(f"file{i+1}/file{i+1}.txt","w") as file:
        file.write(str(y[i]))
