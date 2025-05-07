import requests
import time 
import asyncio

#########part 01
strt=time.process_time()

for i in range(5):

    link=f"http://books.toscrape.com/catalogue/page-{i}.html"
    
    r=requests.get(link)
    print(r)

end=time.process_time()
print(f"time taken to finish the requsts{end-strt}s")

#######################################################
#########   part 02

import asyncio
import requests
import time

async def asyncio_re(i):

    link = f"http://books.toscrape.com/catalogue/page-{i}.html"

    loop = asyncio.get_event_loop()
    r = await loop.run_in_executor(None, requests.get, link)
    print(r)

async def main():
    tasks = [asyncio_re(j) for j in range(5)]
    
    await asyncio.gather(*tasks)

strt = time.process_time()
asyncio.run(main())
end = time.process_time()

print(f"Time taken to finish the requests: {end - strt:.2f}s")
############################################

##########part 03

import aiohttp
import asyncio

async def main(session, link):
    print(2)
    async with session.get(link) as response:
        print(f"URL: {link} Status: {response.status}")

async def request():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(5): 
            link = f"http://books.toscrape.com/catalogue/page-{i}.html"
            tasks.append(main(session, link))
        await asyncio.gather(*tasks)

asyncio.run(request())

