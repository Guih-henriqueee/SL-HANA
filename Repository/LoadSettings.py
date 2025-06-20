from dotenv import load_dotenv
import os

# Carregar as variáveis do arquivo .env
load_dotenv()

# Dicionário com as configurações
SETTINGS = {
    "SR_BASE_URL": os.getenv('SR_BASE_URL'),
    "SR_USER": os.getenv('SR_USER'),
    "SR_PASSWORD": os.getenv('SR_PASSWORD'),
    "SR_TIMEOUT": os.getenv('SR_TIMEOUT'),
    "DATABASE_USER": os.getenv('DATABASE_USER'),
    "DATABASE_PASSWORD": os.getenv('DATABASE_PASSWORD'),
    "DATABASE_HOST": os.getenv('DATABASE_HOST'),
    "DATABASE_PORT": os.getenv('DATABASE_PORT'),
    "DATABASE_SCHEMA": os.getenv('DATABASE_SCHEMA'),
    "DATABASE_DRIVER": os.getenv('DATABASE_DRIVER'),
    'ALERT_PEACKGING': os.getenv('ALERT_PEACKGING'),
    'TIME_PEACKGING': int(os.getenv('TIME_PEACKGING', 0)),
    'ALERT_PICKUP': os.getenv('ALERT_PICKUP'),
    'TIME_PICKUP': int(os.getenv('TIME_PICKUP', 0))
}

class LoadSettings:
    def charge_db_settings(self, settings):
        self._DATABASE_USER     = settings["DATABASE_USER"]
        self._DATABASE_PASSWORD = settings["DATABASE_PASSWORD"]
        self._DATABASE_HOST     = settings["DATABASE_HOST"]
        self._DATABASE_PORT     = settings["DATABASE_PORT"]
        self._DATABASE_SCHEMA   = settings["DATABASE_SCHEMA"]
    
    def charge_sr_settings(self, settings):
        self._SR_BASE_URL = settings["SR_BASE_URL"]
        self._SR_USER = settings["SR_USER"]
        self._SR_PASSWORD = settings["SR_PASSWORD"]
        self._SR_TIMEOUT = settings["SR_TIMEOUT"]    
    
    def get_service_settings(self, settings):
        self._ALERT_PEACKGING = settings["ALERT_PEACKGING"]
        self._TIME_PEACKGING = settings["TIME_PEACKGING"]
        self._ALERT_PICKUP = settings["ALERT_PICKUP"]
        self._TIME_PICKUP = settings["TIME_PICKUP"]
        
    def show_settings(self):
        print(f"Base URL: {self._SR_BASE_URL}")
        print(f"User: {self._SR_USER}")
        print(f"Password: {self._SR_PASSWORD}")
        print(f"Time Out: {self._SR_TIMEOUT}")
                
        print(f"User: {self._DATABASE_USER}")
        print(f"Password: {self._DATABASE_PASSWORD}")
        print(f"Host: {self._DATABASE_HOST}")
        print(f"Port: {self._DATABASE_PORT}")
        print(f"Schema: {self._DATABASE_SCHEMA}")
        
        print(f'Alert Peacking: {self._ALERT_PEACKGING}')
        print(f'Time Peacking: {self._TIME_PEACKGING}')
        print(f'Alert Pickup: {self._ALERT_PICKUP}')
        print(f'Time Pickup: {self._TIME_PICKUP}')
    
    def charge_all_settings(self, settings):
        self.charge_db_settings(settings)
        self.charge_sr_settings(settings)
        self.get_service_settings(settings)