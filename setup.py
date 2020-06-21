#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    'psycopg2',
    'pgcli',
    'Django>=2.2.13',
]

test_requirements = [
    'psycopg2',
    'pgcli',
    'Django>=2.2.13',
]

setup(
    name='django-pgcli',
    version='1.0.1',
    description="Database runtime for Django that replaces psql with pgcli.",
    long_description='\n' + readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    author="Ash Christopher",
    author_email='ash.christopher@gmail.com',
    url='https://github.com/ashchristopher/django-pgcli',
    packages=[
        'django_pgcli',
    ],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='django pgcli postgres database',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
