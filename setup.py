import os
from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='django-config',
    version=version,
    description='An architecture for maintaining multiple settings files in Django',
    author='Tareque Hossain',
    author_email='tareque@codexm.com',
    url='http://github.com/tarequeh/django-config/',
    packages=find_packages(),
    zip_safe=False,
    platforms=["any"],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        ],
    )
