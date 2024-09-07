import click
import subprocess
import os

@click.group()
def evidence_cli():
    """Evidence command wrapper"""
    pass

@evidence_cli.command()
def run_sources():
    """Run Evidence sources"""
    os.chdir('reports')
    subprocess.run(["npm", "run", "sources"])
    os.chdir('..')

# Add more Evidence commands as needed
