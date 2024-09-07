# Purpose: Copy compiled static files to the site folder
import click
import subprocess
import os

@click.group()
def site_cli():
    """Site command wrapper"""
    pass