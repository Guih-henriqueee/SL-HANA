import requests
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

        if response.status_code == 200:
            print("Token obtido com sucesso.")
            print(response.json()["SessionId"])
            return response.json()["SessionId"]
        else:
            raise Exception(f"Falha ao obter token. Status code: {response.status_code}, Response: {response.text}")
        
        
    def logout(self, SESSION_ID):
        print(f"Session to logout:", SESSION_ID)
        url = f"{self._SR_BASE_URL}/Logout"
        headers = {
            "B1SESSION": SESSION_ID
        }
        response = requests.post(url, headers=headers, verify=False)
        if response.status_code == 200:
            print("Logout bem-sucedido.")
        else:
            raise Exception(f"Falha ao fazer logout. Status code: {response.status_code}, Response: {response.text}")


