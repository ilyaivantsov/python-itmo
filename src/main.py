import os
import uvicorn
from fastapi import FastAPI, HTTPException
from src.giphy_api import GiphyClient
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
API_GIPHY_KEY = os.getenv('API_GIPHY_KEY')

app = FastAPI(
    title="Giphy API",
    version="0.0.1",
    docs_url="/api",
)

giphy_client = GiphyClient(API_GIPHY_KEY)


@app.get("/search-gifs")
async def search_gifs(query: str, limit: int = 10, lang: str = 'en') -> list[str]:
    try:
        search_result = await giphy_client.search(query, limit=limit, lang=lang)
        gifs_list = GiphyClient.from_json_to_gifs_list(search_result)
        return gifs_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
