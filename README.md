# django-pgcli

[![Build Status](https://travis-ci.org/ashchristopher/django-pgcli.svg?branch=master)](https://travis-ci.org/ashchristopher/django-pgcli) [![PyPI version](https://badge.fury.io/py/django-pgcli.svg)](https://badge.fury.io/py/django-pgcli) ![PyPI - License](https://img.shields.io/pypi/l/django-mycli)

Replaces your existing *psql* cli for Postgres with *pgcli* which provides enhancements such as auto-completion and syntax highlighting. Visit the [pgcli website](https://www.pgcli.com/) to learn more about the **pgcli** client.

## Installation

To install the package:

    `pip install django-pgcli`

Add `django_pgcli` to your `INSTALLED_APPS` setting in your settings.py file.

    INSTALLED_APPS = [
        ...,
        'django_pgcli',
        
    ]

## Usage

To use the `pgcli` command with your project, call the `dbshell` command.

    ./manage.py dbshell
