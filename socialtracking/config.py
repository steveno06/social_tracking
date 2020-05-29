
class Config: #Used to seperate key information from the main python file. Acts as an addtional layer of security and abstraction
    SECRET_KEY = '5238361285'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'