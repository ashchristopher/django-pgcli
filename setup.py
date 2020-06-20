#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'pgcli',
    'Django>=1.9,<4.0',
]

test_requirements = [
    'pgcli',
    'Django>=1.9,<4.0',
]

setup(
    name='django-pgcli',
    version='0.0.3',
    description="Database runtime for Django that replaces psql with pgcli.",
    long_description=readme + '\n\n' + history,
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
    ],
    test_suite='tests',
    tests_require=test_requirements
)
