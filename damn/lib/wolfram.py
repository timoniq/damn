import aiohttp

API_URL = "http://api.wolframalpha.com/v1"


async def wolfram_calculate(app: str, query: str) -> str:
    async with aiohttp.ClientSession() as session:
        result = await session.get(
            API_URL + "/result", params={"appid": app, "i": query}
        )
        return await result.text()
