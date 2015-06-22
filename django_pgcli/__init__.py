# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.3'


from django.db.backends.postgresql_psycopg2 import base
from django.db.backends.postgresql_psycopg2.client import DatabaseClient


class pgcliDatabaseClient(DatabaseClient):
    executable_name = 'pgcli'

    def runshell(self):
        from pgcli.main import cli

        settings_dict = self.connection.settings_dict
        args = []

        if settings_dict['USER']:
            args += ['--user', settings_dict['USER']]
        if settings_dict['HOST']:
            args += ['--host', settings_dict['HOST']]
        if settings_dict['PORT']:
            args += ['--port', settings_dict['PORT']]
        args += [settings_dict['NAME']]
        cli(args=args)


base.__old_database_client = base.DatabaseClient
base.DatabaseClient = pgcliDatabaseClient
