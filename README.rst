zas
===

.. image:: https://travis-ci.org/appstore-zencore/zas.svg?branch=master
    :target: https://travis-ci.org/appstore-zencore/zas

Zencore Application Server


Install
-------

::

    pip install zas


Usage
-----

::

    E:\zas\src\scripts>python zas.py
    Usage: zas.py [OPTIONS] COMMAND [ARGS]...

    Options:
    -c, --config FILENAME  Config file path, use yaml format. Default to
                            config.yaml.
    --help                 Show this message and exit.

    Commands:
    reload  Reload application server.
    start   Start application server.
    stop    Stop application server.


Example Config
--------------

::

    application:
        deamon: true
        pidfile: /tmp/appname.pid
        main: app.main

