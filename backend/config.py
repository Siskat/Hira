import os

SECRET_KEY = '\xaa\x8c\xa0\xfd\xd3\xa0C\xf08\xc0\x18\xe2\x80H\xaaQ\x93\t\x12\xc7\x91'
DEBUG=True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# database configuration settings
DB_USERNAME = 'mpadmin'
DB_PASSWORD = 'GulabJamun'
DATABASE_NAME = 'anything_really'
DB_HOST = os.getenv('IP','128.199.216.13')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI