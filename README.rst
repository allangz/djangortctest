==============================================================
 Example Django project using Celery with Nodejs and Socketio
 with Redis for RTC data
==============================================================

Contents
========

''proj/''
=========

This is the project iself, created using
''django-admin.py startproject proj'', and then the settings module
(''proj/settings.py'') was modified to add ''demoapp'' to
''INSTALLED_APPS''

''proj/celery.py''
==================

This module contains the Celery application instance for this project,
we take configuration from Django settings and use ''autodiscover_tasks'' to
find task modules inside all packages listed in ''INSTALLED_APPS''.

''demoapp/''
============

Example generic app.  This is decoupled from the rest of the project by using
the ''@shared_task'' decorator.  This decorator returns a proxy that always
points to the currently active Celery instance.

Configure email account and password for gmail account in sendmail on file tasks.py

''nodejs/''
===========

Nodejs webserver with socket listen to chanel post on Redis and send it to 
client using socketio.

Starting the worker
===================

.. code-block:: bash

    $ celery -A proj worker -l info

Starting Nodejs
===================

.. code-block:: bash

    $ nodejs quote.js 

Starting django
===================

.. code-block:: bash

    $ python manage.py runserver


