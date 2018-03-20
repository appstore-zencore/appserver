
"""Open Server Wrapper.
"""
import os
import yaml
import click
from zencore.utils.magic import import_from_string
from zencore.utils.magic import select
from zdas import daemon_start
from zdas import daemon_stop



DEFAULT_CONFIG_PATH = "config.yaml"
DEFAULT_PIDFILE = "zas.pid"
GLOBAL_CONFIG = {}


def main():
    os.sys.path.append(os.getcwd())
    real_main = select(GLOBAL_CONFIG, "application.main")
    if not real_main:
        print("Item application.main required in config file.", file=os.sys.stderr)
        os.sys.exit(1)
    real_main = import_from_string(real_main)
    if not real_main:
        print("Load application.main = {} failed.".format(real_main), file=os.sys.stderr)
        os.sys.exit(2)
    real_main(GLOBAL_CONFIG)


@click.group()
@click.option("-c", "--config", default=DEFAULT_CONFIG_PATH, type=click.File("rb"), help="Config file path, use yaml format. Default to {}.".format(DEFAULT_CONFIG_PATH))
def server(config):
    if config:
        data = yaml.load(config)
        if data:
            GLOBAL_CONFIG.update(data)


@server.command()
def start():
    """Start application server.
    """
    daemon = select(GLOBAL_CONFIG, "application.daemon", False)
    workspace = select(GLOBAL_CONFIG, "application.workspace", None)
    pidfile = select(GLOBAL_CONFIG, "application.pidfile", DEFAULT_PIDFILE)
    daemon_start(main, pidfile, daemon, workspace)


@server.command()
def stop():
    """Stop application server.
    """
    pidfile = select(GLOBAL_CONFIG, "application.pidfile", DEFAULT_PIDFILE)
    daemon_stop(pidfile)


@server.command()
def reload():
    """Reload application server.
    """
    stop()
    start()
