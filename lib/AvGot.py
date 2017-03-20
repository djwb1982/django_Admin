import asyncio
import aiohttp
import async_timeout

import re

class AvGot(object):
  def __init__(self, loop=None):
    self.loop = loop

    self.headers = {
      "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)"
                    " AppleWebKit/537.36 (KHTML, like Gecko)"
                    " Chrome/54.0.2840.87 Safari/537.36"),
    }
    self.conn = aiohttp.TCPConnector(verify_ssl=False)
    self.session = aiohttp.ClientSession(loop=loop,
                    connector=self.conn,
                    headers=self.headers)

    self.pipe = []

  async def fetch(self, url=""):
    with async_timeout(10):
      async with self.session.get(url) as resp:
          return await resp.text()
  async def extract(self, url="", regexp=r''):
    html = await self.fetch(url)
    matches = re.findall(regexp, html)
    return matches
  def entry(self, url='', regexp=r''):
    def wrapper(callback):
      self.pipe.append(callback)
    return wrapper
  def close(self):
    self.session()
    self.loop.close()
  def run(self):
    pass

loop = asyncio.get_event_loop()
av = AvGot(loop)

reTag = re.compile('<a href="(\/tag\/.*?)">(.*?)<\/a>')
ROOT  = "https://movie.douban.com/tag/"

@av.entry(ROOT, reTag)
async def entry_callback(result):
  # await db.save(result) 保存到数据库
  def clean(row):
    return ("https://movie.douban.com{}".format(row[0]), row[1])
  return list(map(clean, result))[:2]

av.run()
av.close()