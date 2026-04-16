import httpx

async def fetch_gender_data(name: str):
    url = f"https://api.genderize.io?name={name}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise Exception("External API failure")

    return response.json()