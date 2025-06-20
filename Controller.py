import asyncio
from Repository.LoadSettings import LoadSettings, SETTINGS
from Helper.DbConnection import DbConnection
from Helper.SLConnection import SLConnection
from Services.GetItems import GetItems

async def main():
    # Carregar settings
    loader = LoadSettings()
    loader.charge_all_settings(SETTINGS)
    print((f"ALERT_PEACKGING: {SETTINGS['ALERT_PEACKGING']}"))
    print((f"TIME_PEACKGING: {SETTINGS['TIME_PEACKGING']}"))
    print((f"ALERT_PICKUP: {SETTINGS['ALERT_PICKUP']}"))
    print((f"TIME_PICKUP: {SETTINGS['TIME_PICKUP']}"))

    try:
        # Exemplo: Buscar item no SAP
        get_items_service = GetItems(SETTINGS)
        result = await get_items_service.get_items('NAC012269')
        if result:
            return 'sucess'
        
    finally:

        print("Logout bem-sucedido.")

if __name__ == '__main__':
    asyncio.run(main())
