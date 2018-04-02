appserver
=========

.. image:: https://travis-ci.org/appstore-zencore/appserver.svg?branch=master
    :target: https://travis-ci.org/appstore-zencore/appserver

NOTICE
------

Application renamed to appstart, see detail at https://github.com/appstore-zencore/appstart.

About
-----

Application server framework help you write long run application.

Install
-------

::

    pip install appserver


Usage
-----

::

    E:\zencore>apprun
    Usage: apprun [OPTIONS] COMMAND [ARGS]...

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


Create a new type server
------------------------

::

    from zascore import server
    from zascore import set_default_config_path
    from zascore import set_default_pidfile
    from zascore import set_config_loader
    from zascore import default_config_loader

    def helloserver_loader(config):
        data = default_config_loader(config)
        data["server-name"] = "hello server v1.0.0"
        return data

    if __name__ == "__main__":
        set_default_config_path("/etc/helloserver.yaml")
        set_default_pidfile("/var/run/helloserver.pid")
        set_config_loader(helloserver_loader)
        server()
