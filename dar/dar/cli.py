import click
from .dbt_commands import dbt_cli
from .evidence_commands import evidence_cli
from .install import setup

@click.group()
def cli():
    """Darrell: Orchestrating dbt and Evidence BI for an Open Source Analytics Stack"""
    pass

cli.add_command(setup)
cli.add_command(dbt_cli, name="models")
cli.add_command(evidence_cli, name="reports")

if __name__ == '__main__':
    cli()
