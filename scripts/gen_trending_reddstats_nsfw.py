import asyncio
import httpx
from bs4 import BeautifulSoup

BASE_URL = "https://reddstats.com/ranking/relative"
PERIODS = ["daily", "weekly", "monthly"]
SUBSCRIBER_COUNTS = [
    "1001-10000",
    "10001-50000",
    "50001-100000",
    "100001-1000000",
    "1000001-100000000",
]
LIMIT_PER_BIN = 50


async def fetch_and_extract(
    client: httpx.AsyncClient, period: str, counts: str
) -> set[str]:
    url = f"{BASE_URL}?over18=True&period={period}&subscriber_classification={counts}"
    resp = await client.get(url, timeout=httpx.Timeout(60.0))
    soup = BeautifulSoup(resp.text, "html.parser")
    elements = soup.select('div.item a[href^="/subreddit/"]')
    return set(el.text.strip() for el in elements[:LIMIT_PER_BIN])


async def generate_trending() -> None:
    async with httpx.AsyncClient() as client:
        results = await asyncio.gather(
            *[
                fetch_and_extract(client, period, counts)
                for period in PERIODS
                for counts in SUBSCRIBER_COUNTS
            ]
        )

    all_subreddits = set().union(*results)

    for subreddit in sorted(all_subreddits):
        print(subreddit)


if __name__ == "__main__":
    asyncio.run(generate_trending())
