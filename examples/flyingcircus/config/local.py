ADMINS = (('Django User', 'djuser@djangoproject.com'),)

# Database Configuration

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'configdemo'
DATABASE_USER = 'root'
DATABASE_PASSWORD = ''
DATABASE_HOST = 'localhost'
DATABASE_PORT = '3306'
DEFAULT_CHARSET = 'utf-8'
DATABASE_OPTIONS = {
    'sql_mode': 'TRADITIONAL,STRICT_ALL_TABLES,ANSI',
    'charset': 'utf8',
    'init_command': 'SET storage_engine=INNODB',
}
