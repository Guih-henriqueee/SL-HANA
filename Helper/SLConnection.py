import requests
import httpx
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SLConnection:
    def __init__(self, settings: dict):
        self._SR_BASE_URL           = settings["SR_BASE_URL"]
        self._SR_USER               = settings["SR_USER"]
        self._SR_PASSWORD           = settings["SR_PASSWORD"]
        self._TIMEOUT               = int(settings.get("SR_TIMEOUT", 10))
        self._DATABASE_SCHEMA       = settings["DATABASE_SCHEMA"]

    def get_token(self):
        url = f"{self._SR_BASE_URL}/Login"
        payload = {
            "CompanyDB": self._DATABASE_SCHEMA,
            "Password": self._SR_PASSWORD,
            "UserName": self._SR_USER
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=self._TIMEOUT, verify=False)

        if response.ok:
            self._COOKIES = response.cookies
            
            self._SESSION_ID = response.cookies.get("B1SESSION")
            self._ROUTEID = response.cookies.get("ROUTEID")
            
           
            return self._SESSION_ID, self._ROUTEID
        else:
            raise Exception(f"Falha ao obter token. Status code: {response.status_code}, Response: {response.text}")
        
        
    async def logout(self):
        url = f"{self._SR_BASE_URL}/Logout"
        headers = {
            "B1SESSION": self._SESSION_ID
        }
        cookies = {
            "B1SESSION": self._SESSION_ID,
            "ROUTEID": self._ROUTEID
        }

        async with httpx.AsyncClient(timeout=self._TIMEOUT, verify=False) as client:
            response = await client.post(url, headers=headers, cookies=cookies)

        if response.status_code == 200:
            print("Logout bem-sucedido.")
        else:
            raise Exception(f"Falha ao fazer logout. Status code: {response.status_code}, Response: {response.text}")



    async def requests(self, url, method, headers=None, payload=None):
        url = f"{self._SR_BASE_URL}{url}"
        print(f"URL: {url}")

        default_headers = {
            "Content-Type": "application/json",

        }

        if headers:
            default_headers.update(headers)

        cookies = {
            "B1SESSION": self._SESSION_ID,
            "ROUTEID": self._ROUTEID
        }

        async with httpx.AsyncClient(timeout=self._TIMEOUT, verify=False) as client:
            response = await client.request(
                method=method,
                url=url,
                headers=default_headers,
                json=payload,
                cookies=cookies
            )


        print(response.status_code, response.text)
        return response
