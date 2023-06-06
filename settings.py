from vendor.config import Config

class Settings:
    DATABASE='postgresql+asyncpg:///internet_shop'
    USER='postgres'
    PASSWORD='roman1201'
    HOST='127.0.0.1'
    PORT='5432'
    API_TOKEN='6226396360:AAFPDVmZsjJ5c8cfFt2Ya7gBg7KU_dsUJko'

DATABASE = Config.DATABASE
API_TOKEN = Config.API_TOKEN
