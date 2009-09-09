ADMINS = (('Monty Python', 'mpython@djangoproject.com'),)

# Database Configuration

import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'db'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '%s/monty.db' % db_path
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {
}

ENABLE_PASSWORD = True
PASSWORD_DIGEST = '97e43572f170e47d0df46fad5a3fe7d9'
