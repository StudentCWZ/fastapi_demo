#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Version:  Python 3.11.2
# @Software: Sublime Text 4
# @Author:   StudentCWZ
# @Email:    StudentCWZ@outlook.com
# @Date:     2023-03-09 08:57:20
# @Last Modified by: StudentCWZ
# @Last Modified time: 2023-03-09 08:58:26
# @Description: 命令行封装模块
"""

# pylint: skip-file


from pathlib import Path

import click
from alembic import config
from click import Context

from app import __version__, utils
from app.config import settings
from app.server import Server


@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    "-V", "--version", is_flag=True, help="Show version and exit."
)  # If it's true, it will override `settings.Logger.Verbose`
@click.option("-v", "--verbose", is_flag=True, help="Show more info.")
@click.option(
    "--debug", is_flag=True, help="Enable debug."
)  # If it's true, it will override `settings.Logger.Debug`
def main(ctx: Context, version: str, verbose: bool, debug: bool):
    """Main commands"""
    if version:
        click.echo(__version__)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
    else:
        if verbose:
            settings.Logger.Verbose = True
        if debug:
            settings.Logger.Debug = True


@main.command()
@click.option(
    "-h", "--host", show_default=True, help=f"Host IP. Default: {settings.Server.Host}"
)
@click.option(
    "-p",
    "--port",
    show_default=True,
    type=int,
    help=f"Port. Default: {settings.Server.Port}",
)
def server(host, port):
    """Start server."""
    kwargs = {
        "Host": host,
        "Port": port,
    }
    for name, value in kwargs.items():
        if value:
            settings.Server[name] = value

    Server().run()


@main.command()
@click.pass_context
@click.option("-h", "--help", is_flag=True)
@click.argument("args", nargs=-1)
def migrate(ctx: Context, help, args):
    """usage migrate -- arguments"""
    with utils.chdir(Path(__file__).parent.parent / "migration"):
        argv = list(args)
        if help:
            argv.append("--help")
        print(ctx.command_path, argv)
        config.main(prog=ctx.command_path, argv=argv)
