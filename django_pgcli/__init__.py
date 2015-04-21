# -*- coding: utf-8 -*-

__author__ = 'Ash Christopher'
__email__ = 'ash.christopher@gmail.com'
__version__ = '0.0.1'


from django.db.backends.postgresql_psycopg2 import base
from .client import pgcliDatabaseClient


base.DatabaseClient = pgcliDatabaseClient

