import click
import subprocess
import os

@click.group()
def evidence_cli():
    """Evidence command wrapper"""
    pass


@evidence_cli.command()
def build():
    """Generate Evidence static files"""
    os.chdir('reports')
    subprocess.run(["npm", "run", "build"])
    os.chdir('..')

@evidence_cli.command()
def preview():
    """Run Evidence dev server"""
    os.chdir('reports')
    subprocess.run(["npm", "run", "dev"])
    os.chdir('..')

# TODO: Add refresh command that copies compiled dbt models to Evidence source folder
@evidence_cli.command()
def refresh():
    """Copy dbt models to Evidence"""
    # os.chdir('reports')
    # subprocess.run(["npm", "run", "sources"])
    # os.chdir('..')
    pass

@evidence_cli.command()
def update():
    """Run Evidence sources"""
    os.chdir('reports')
    subprocess.run(["npm", "run", "sources"])
    os.chdir('..')