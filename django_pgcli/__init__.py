# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '1.0.0'


from django.db.backends.postgresql import base
from django.db.backends.postgresql.client import DatabaseClient


class PgCLIDatabaseClient(DatabaseClient):
    executable_name = 'pgcli'
    
    def runshell(self):
        PgCLIDatabaseClient.runshell_db(self.connection.get_connection_params())

base.DatabaseWrapper.__old_database_client_class = base.DatabaseClient
base.DatabaseWrapper.client_class = PgCLIDatabaseClient
