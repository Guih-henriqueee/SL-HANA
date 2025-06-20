from Repository.LoadSettings import LoadSettings, SETTINGS
from Helper.DbConnection import DbConnection  
from Helper.SLConnection import SLConnection

if __name__ == '__main__':
    loader = LoadSettings()
    loader.charge_all_settings(SETTINGS)

    db = DbConnection(SETTINGS)  
    db.test_connection()         

    sr = SLConnection(SETTINGS)
    SESSION_ID = sr.get_token() 
    sr.logout(SESSION_ID)