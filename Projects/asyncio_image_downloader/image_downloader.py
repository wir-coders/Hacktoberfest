# a Python Program to fetch an image from web using async function
import random
import io
import aiohttp
import asyncio
from PIL import Image


async def async_fetch(url: str) -> bytes:
  """fetch html content of  a page. Returns a bytestring of the content"""
  async with aiohttp.ClientSession() as session:
      async with session.get(url) as response:
          html_in_bytestring = await response.content.read()
          return html_in_bytestring

async def waifu_fun():
  rnum = random.randint(0, 100000)
  url = 'https://www.thiswaifudoesnotexist.net/example-' + str(rnum) + '.jpg'
  html = await async_fetch(url)
  img = Image.open(io.BytesIO(html))
  img.save(f'{rnum}.jpg')
  print("Image Saved")
asyncio.run(waifu_fun())
