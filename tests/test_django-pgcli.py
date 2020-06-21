#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import django_pgcli  # noqa


class RuntimeTestCase(unittest.TestCase):

    def test_database_client_subclassed(self):
        from django.db.backends.postgresql import base

        self.assertEqual(base.DatabaseWrapper.client_class, django_pgcli.PgCLIDatabaseClient)

    def test_database_client_calls_pgcli_executable(self):
        from django.db.backends.postgresql import base
          
        self.assertEqual(base.DatabaseWrapper.client_class.executable_name, 'pgcli')

    def test_old_database_client_set_on_base(self):
        from django.db.backends.postgresql import base
        from django.db.backends.postgresql.client import DatabaseClient
        
        self.assertEqual(getattr(base.DatabaseWrapper, '__old_database_client_class'), DatabaseClient)

if __name__ == '__main__':
    unittest.main()
