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


Create a new type server
------------------------

::

    from zascore import server
    from zascore import set_default_config_path
    from zascore import set_default_pidfile
    from zascore import set_config_loader

    def helloserver_loader(config):
        data = {}
        if isinstance(config, str):
            data = yaml.load(config)
        data["server-name"] = "hello server v1.0.0"
        return data

    if __name__ == "__main__":
        set_default_config_path("/etc/helloserver.yaml")
        set_default_pidfile("/var/run/helloserver.pid")
        set_config_loader(helloserver_loader)
        server()
