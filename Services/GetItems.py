from Helper.SLConnection import SLConnection, requests
import asyncio

class GetItems:
    def __init__(self, settings: dict):
        self._SL_CONNECTION = SLConnection(settings)
        self._SESSION_ID = self._SL_CONNECTION.get_token()
        self._BASE_URL = settings["SR_BASE_URL"]
    
    
    async def get_items(self, product_code: str):
        url = f"/Items('{product_code}')"
        response = await self._SL_CONNECTION.requests(
            url=url,
            method="GET"
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Falha ao obter item. Status code: {response.status_code}, Response: {response.text}")
