"""Open Server Wrapper.
"""
import os
import yaml
import click
from magic_import import import_from_string
from dictop import select
from daemon_application import daemon_start
from daemon_application import daemon_stop

DEFAULT_CONFIG_PATH = "config.yml"
DEFAULT_PIDFILE = "server.pid"
GLOBAL_CONFIG = {}
CONFIG_LOADER = None

def set_default_config_path(path):
    global DEFAULT_CONFIG_PATH
    DEFAULT_CONFIG_PATH = path

def set_default_pidfile(pidfile):
    global DEFAULT_PIDFILE
    DEFAULT_PIDFILE = pidfile

def set_config_loader(loader):
    global CONFIG_LOADER
    CONFIG_LOADER = loader

def default_config_loader(config):
    data = {}
    if config:
        if isinstance(config, dict):
            data = config
        else:
            data = yaml.load(config) # click.File gets BufferedReader instance
    return data or {}

def main():
    os.sys.path.append(os.getcwd())
    real_main = select(GLOBAL_CONFIG, "application.main")
    if not real_main:
        click.echo("Item application.main required in config file.", file=os.sys.stderr)
        os.sys.exit(1)
    real_main = import_from_string(real_main)
    if not real_main:
        click.echo("Load application.main = {name} failed.".format(name=real_main), file=os.sys.stderr)
        os.sys.exit(2)
    real_main(GLOBAL_CONFIG)

@click.group()
@click.option("-c", "--config", type=click.File("rb"), help="Config file path, use yaml format.")
def server(config):
    if not config:
        config = open(DEFAULT_CONFIG_PATH, "rb")
    load_config = CONFIG_LOADER or default_config_loader
    GLOBAL_CONFIG.update(load_config(config))

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

if __name__ == "__main__":
    server()
