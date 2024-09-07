import os
import subprocess
import click

@click.command()
@click.option('--path', default='analytics', help='Path to create the analytics directory')
def setup(path):
    """Install and set up the analytics environment"""
    # Create analytics directory
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

    # Install dbt
    click.echo("Installing dbt...")
    subprocess.run(["pip", "install", "dbt-core", "dbt-duckdb"])

    # Initialize dbt project
    click.echo("Initializing dbt project...")
    subprocess.run(["dbt", "init"])

    # Install Evidence
    click.echo("Installing Evidence...")
    subprocess.run(["npx", "degit", "evidence-dev/template", "reports"])
    subprocess.run(["npm", "--prefix", "./reports", "install"])

    # Create additional directories in analytics directory
    dirs = ['data', 'scripts']
    for dir_name in dirs:
        os.makedirs(os.path.join(path, dir_name), exist_ok=True)
        os.makedirs(dir_name, exist_ok=True)

    click.echo("Analytics folder set up successfully!")

    ## Make 'site' directory at same level as 'analytics' directory
    os.makedirs('site', exist_ok=True)

    click.echo("Site folder set up successfully!")
