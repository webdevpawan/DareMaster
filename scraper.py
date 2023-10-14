import aiohttp
import asyncio
import json

api = "https://api.truthordarebot.xyz/v1"


async def get_truth():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}/truth") as resp:
                if resp.status != 200:
                    print(f"Unable to get truth: HTTP {resp.status}")
                    return None

                response = await resp.text()
                response_json = json.loads(response)

                return response_json['question']

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


async def get_dare():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{api}/dare") as resp:
                if resp.status != 200:
                    print(f"Unable to get dare: HTTP {resp.status}")
                    return None

                response = await resp.text()
                response_json = json.loads(response)

                return response_json['question']

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


async def get_truth_and_dare():
    truth, dare = await asyncio.gather(get_truth(), get_dare())
    return truth, dare


if __name__ == "__main__":
    truth, dare = asyncio.run(get_truth_and_dare())
    print(truth, dare)
