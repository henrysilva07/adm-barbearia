DEBUG=True

# Database Configuration
DB_NAME = 'barbearia'
USERNAME = ''
PASSWORD = ''
SERVER = ''


SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}.db"
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY="ADM-BARBEARIA"
