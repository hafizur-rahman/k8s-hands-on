import os

def get_env_variable(var_name, default=None):
    """Get the environment variable or raise exception.

    Args:
        var_name (str): the name of the environment variable to look up
        default (str): the default value if no env is found
    """
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        raise RuntimeError(
            'The environment variable {} was missing, abort...'
            .format(var_name)
        )


# MySQL

MYSQL_USER = get_env_variable('DB_USER')
MYSQL_PASSWORD = get_env_variable('DB_PASSWORD')
MYSQL_HOST = get_env_variable('DB_HOST')
MYSQL_PORT = get_env_variable('DB_PORT', 3306)
MYSQL_DB = get_env_variable('DB_NAME')

SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_HOST,
    MYSQL_PORT,
    MYSQL_DB,
)


# Redis

REDIS_HOST = get_env_variable('REDIS_HOST')
REDIS_PORT = get_env_variable('REDIS_PORT', 6379)


# Celery

class CeleryConfig:
    BROKER_URL = 'redis://{0}:{1}/0'.format(REDIS_HOST, REDIS_PORT)
    CELERY_IMPORTS = ('superset.sql_lab',)
    CELERY_RESULT_BACKEND = 'redis://{0}:{1}/1'.format(REDIS_HOST, REDIS_PORT)
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}
    CELERY_TASK_PROTOCOL = 1


CELERY_CONFIG = CeleryConfig
