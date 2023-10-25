import os
import asyncio

from dotenv import load_dotenv

from src.giphy_api import GiphyClient

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


async def main():
    giphy_client = GiphyClient(os.getenv('API_GIPHY_KEY'))
    search_result = await giphy_client.search('cats', limit=1)
    print(GiphyClient.from_json_to_gifs_list(search_result))


if __name__ == "__main__":
    asyncio.run(main())
