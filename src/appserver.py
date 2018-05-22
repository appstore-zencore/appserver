"""Open Server Wrapper.
"""
import os
import yaml
import click
from magic_import import import_from_string
from dictop import select
from daemon_application import daemon_start
from daemon_application import daemon_stop
from functools import partial


DEFAULT_CONFIG_PATH = "config.yml"
DEFAULT_PIDFILE = "server.pid"
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


def main(config):
    os.sys.path.append(os.getcwd())
    real_main = select(config, "application.main")
    if not real_main:
        click.echo("Item application.main required in config file.", file=os.sys.stderr)
        os.sys.exit(1)
    real_main = import_from_string(real_main)
    if not real_main:
        click.echo("Load application.main = {name} failed.".format(name=real_main), file=os.sys.stderr)
        os.sys.exit(2)
    real_main(config)


@click.group()
@click.option("-c", "--config", type=click.File("rb"), help="Config file path, use yaml format.")
@click.pass_context
def server(context, config):
    config_close_flag = False
    if not config:
        config = open(DEFAULT_CONFIG_PATH, "rb")
        config_close_flag = True
    try:
        load_config = CONFIG_LOADER or default_config_loader
        context.obj = {}
        context.obj["config"] = load_config(config)
    finally:
        if config_close_flag:
            config.close()


@server.command()
@click.pass_context
def start(context):
    """Start application server.
    """
    config = context.obj["config"]
    daemon = select(config, "application.daemon", False)
    workspace = select(config, "application.workspace", None)
    pidfile = select(config, "application.pidfile", DEFAULT_PIDFILE)
    daemon_start(partial(main, config), pidfile, daemon, workspace)


@server.command()
@click.pass_context
def stop(context):
    """Stop application server.
    """
    config = context.obj["config"]
    pidfile = select(config, "application.pidfile", DEFAULT_PIDFILE)
    daemon_stop(pidfile)


@server.command()
@click.pass_context
def reload(context):
    """Reload application server.
    """
    stop(context)
    start(context)


if __name__ == "__main__":
    server()
