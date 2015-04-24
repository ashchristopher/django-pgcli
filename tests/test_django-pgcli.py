#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import django_pgcli  # noqa


class RuntimeTestCase(unittest.TestCase):

    def test_database_client_subclassed(self):
        from django.db.backends.postgresql_psycopg2 import base

        self.assertEqual(base.DatabaseClient, django_pgcli.pgcliDatabaseClient)

    def test_database_client_calls_pgcli_executable(self):
        from django.db.backends.postgresql_psycopg2 import base
          
        self.assertEqual(base.DatabaseClient.executable_name, 'pgcli')

    def test_old_database_client_set_on_base(self):
        from django.db.backends.postgresql_psycopg2 import base
        from django.db.backends.postgresql_psycopg2.client import DatabaseClient
        
        self.assertEqual(getattr(base, '__old_database_client'), DatabaseClient)

if __name__ == '__main__':
    unittest.main()
