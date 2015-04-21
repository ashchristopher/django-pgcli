from django.db.backends.postgresql_psycopg2.client import DatabaseClient


class pgcliDatabaseClient(DatabaseClient):
    executable_name = 'pgcli'
