'''
pip install aiohttp
'''

# server
import aiohttp.web

async def handle(request):
  name = request.match_info.get('name', 'Anonymous')
  text = 'Hello, ' + name
  return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)


web.run_app(app)

# client

import aiohttp
import asyncio
import async_timeout

async def fetch(session, url):
  async with session.get(url) as response:
    return await response.text()

async def main():
  async with aiohttp.ClientSession() as session:
    html = await fetch(session, 'http://python.org')
    print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
