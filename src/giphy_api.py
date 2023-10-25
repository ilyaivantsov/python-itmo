from aiohttp import ClientSession


class GiphyClient:
    def __init__(self, api_key):
        self.api_key = api_key

    async def search(self, query, limit=10, lang: str = 'en'):
        async with ClientSession() as session:
            url = 'https://api.giphy.com/v1/gifs/search'
            params = {
                'api_key': self.api_key,
                'q': query,
                'lang': lang,
                'limit': limit
            }
            async with session.get(url, params=params) as response:
                return await response.json()

    @staticmethod
    def from_json_to_gifs_list(json) -> list[str]:
        try:
            return [gif['images']['original']['url'] for gif in json['data']]
        except KeyError:
            print('Error: Giphy API response has changed.')
            return []
