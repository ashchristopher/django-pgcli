# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.2'


from django.db.backends.postgresql_psycopg2 import base
from django.db.backends.postgresql_psycopg2.client import DatabaseClient


class pgcliDatabaseClient(DatabaseClient):
    executable_name = 'pgcli'

base.__old_database_client = base.DatabaseClient
base.DatabaseClient = pgcliDatabaseClient
