import configparser

config=configparser.RawConfigParser()
config.read(".\\prerequisitedata\\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url=config.get('common data','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        pwd = config.get('common data', 'password')
        return pwd