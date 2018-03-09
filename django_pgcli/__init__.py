# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.3'


from django.db.backends.postgresql import base
from django.db.backends.postgresql.client import DatabaseClient


class pgcliDatabaseClient(DatabaseClient):
    executable_name = 'pgcli'
    
    def runshell(self):
        pgcliDatabaseClient.runshell_db(self.connection.get_connection_params())

base.DatabaseWrapper.__old_database_client_class = base.DatabaseClient
base.DatabaseWrapper.client_class = pgcliDatabaseClient
