## HW 3. Giphy API

### About:

This is a simple API that allows you to search for gifs on the Giphy [website](https://giphy.com/) by voice.

There are three microservices in the project:
- **FastAPI** - service for working with the Giphy API
- **Site** - service for working with the user interface
- **WebApi** - service for working with the voice to text API

How it works:
1. Create an API key on the [Giphy](https://developers.giphy.com/) website.
   Add the key to the .env file.
2. Start the FastAPI service.
3. Go to the site and search for gifs by voice. (If something doesn't work, try reloading the page. :))

> **Note:** Works only on desktop browsers. Tested on Chrome and Yandex Browser.

### Demo:
Demo site: [https://giphy-demo.website.yandexcloud.net/](https://giphy-demo.website.yandexcloud.net/)
