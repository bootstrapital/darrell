import os
import subprocess
import click

@click.command()
@click.option('--path', default='analytics', help='Path to create the analytics directory')
def install_analytics(path):
    """Install and set up the analytics environment"""
    # Create analytics directory
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

    # Install dbt
    click.echo("Installing dbt...")
    subprocess.run(["pip", "install", "dbt-core", "dbt-postgres"])

    # Initialize dbt project
    click.echo("Initializing dbt project...")
    subprocess.run(["dbt", "init"])

    # Install Evidence
    click.echo("Installing Evidence...")
    subprocess.run(["npx", "degit", "evidence-dev/template", "reports"])
    subprocess.run(["npm", "--prefix", "./reports", "install"])

    # Create additional directories
    dirs = ['analyses', 'docs', 'macros', 'seeds', 'snapshots', 'tests']
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)

    click.echo("Analytics environment set up successfully!")
