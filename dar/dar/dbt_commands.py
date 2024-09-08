import click
import subprocess

@click.group()
def dbt_cli():
    """dbt command wrapper"""
    pass

@dbt_cli.command()
def init():
    """Initialize a new dbt project"""
    subprocess.run(["dbt", "init"])

@dbt_cli.command()
@click.option('-s', '--select', help='Specify models to run')
def run(select):
    """Run dbt models"""
    cmd = ["dbt", "run"]
    if select:
        cmd.extend(["-s", select])
    subprocess.run(cmd)

@dbt_cli.command()
@click.option('-s', '--select', help='Specify models to test')
def test(select):
    """Run dbt tests"""
    cmd = ["dbt", "test"]
    if select:
        cmd.extend(["-s", select])
    subprocess.run(cmd)

@dbt_cli.command()
def docs():
    """Generate dbt documentation"""
    subprocess.run(["dbt", "docs", "generate"])

@dbt_cli.command()
def compile():
    """Compile dbt models"""
    subprocess.run(["dbt", "compile"])