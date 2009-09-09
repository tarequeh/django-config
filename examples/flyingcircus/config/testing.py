ADMINS = (('Project Tester', 'ptester@djangoproject.com'),)

# Database Configuration

import os

db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'db'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '%s/testing.db' % db_path
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''
DATABASE_OPTIONS = {
}

TEST_DATABASE_NAME = '%s/testing.db' % db_path
