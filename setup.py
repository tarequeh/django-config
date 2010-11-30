#!/usr/bin/env python

from setuptools import setup

version = '0.1.3'

setup(
    name='django-config',
    version=version,
    description='An architecture for maintaining multiple settings files in Django',
    author='Tareque Hossain',
    author_email='tareque@codexm.com',
    url='http://github.com/tarequeh/django-config/',
    packages=['djangoconfig'],
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        ],
    )
