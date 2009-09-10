###################
 Django-Config
###################
An architecture for maintaining multiple settings files in Django

Overview
========
django-config is an easy way to maintain multiple configurations for django. It relies on the concept of having a shared configuration file (base) 
and a per user/ server custom configuration file (dev1/ dev2/ local/ staging). settings.py combines the base & custom configuration and loads it up.

Installation
============
1. Include the djangoconfig application in your django application set. 
2. Create a directory named 'config' at the root directory of your project. 'config' directory will contain your global settings file: 'base.py' & all custom configuration file e.g. 'local.py'.
3. Overwrite 'manage.py' & 'settings.py' with the files supplied with django-config  

Usage
=====
1. Add new settings to your custom settings file.
2. Override base settings in custom settings file.
3. Whenever you run manage.py, select your configuration identifier

More
====

The primary repository for Django-Config is located at:

`http://github.com/tarequeh/django-config/ <http://github.com/tarequeh/django-config/>`_

Django-Config was created by Nowell Strite. Extended and maintained by Tareque Hossain
