# Troubleshooting Guide for Darrell

This guide covers common issues you might encounter when using Darrell, including problems related to dbt, Evidence BI, and general CLI usage. If you're experiencing difficulties, refer to the sections below for potential solutions.

## Table of Contents
1. [General CLI Issues](#general-cli-issues)
2. [dbt-related Issues](#dbt-related-issues)
3. [Evidence BI Issues](#evidence-bi-issues)
4. [Installation and Setup Problems](#installation-and-setup-problems)

## General CLI Issues

### Command Not Found
If you encounter a "command not found" error when trying to use Darrell, ensure that:

1. Darrell is properly installed.
2. The installation directory is in your system's PATH.

Try running:

```bash
which darrell
```

If it doesn't return a path, reinstall Darrell or add its location to your PATH.

### Unexpected CLI Behavior
If Darrell commands are not behaving as expected:

1. Check that you're using the correct syntax for the command.
2. Ensure you're in the right directory (project root) when running commands.
3. Verify that you have the latest version of Darrell installed.

To update Darrell, run:

```bash
pip install --upgrade darrell
```

## dbt-related Issues

### dbt Command Failures
If dbt commands (e.g., `darrell models run`) are failing:

1. Ensure dbt is properly installed and configured.
2. Check your `profiles.yml` file for correct database connection settings.
3. Verify that your dbt project structure is correct.

To test your dbt setup, try running:

```bash
darrell models compile
```

If this fails, check the error message for specific issues with your dbt configuration or models.

### Model Selection Problems
If you're having trouble selecting specific models:

1. Ensure you're using the correct model names or selection syntax.
2. Check that the models exist in your project.

Example of correct model selection:

```bash
darrell models run --select my_model+
```

## Evidence BI Issues

### Build Failures
If `darrell reports build` is failing:

1. Ensure you have Node.js and npm installed.
2. Check that all required dependencies are installed in your Evidence project.
3. Verify that your Evidence configuration files are correct.

Try running:

```bash
cd reports
npm install
```

Then attempt the build again.

### Preview Not Working
If `darrell reports preview` isn't working:

1. Ensure no other processes are using the required ports.
2. Check your firewall settings.
3. Verify that your Evidence project structure is correct.

Try manually running the preview from the `reports` directory:

```bash
cd reports
npm run dev
```

This may provide more detailed error messages.

## Installation and Setup Problems

### DuckDB Setup Issues
If you're having trouble setting up DuckDB during the `dbt init` process:

1. Ensure you have the latest version of dbt-duckdb installed.
2. Check that DuckDB is properly installed on your system.

If issues persist, try manually initializing a dbt project with DuckDB:

```bash
dbt init my_project
cd my_project
```

Then select DuckDB as your database when prompted.

### Darrell Installation Failures
If you're unable to install Darrell:

1. Ensure you have Python 3.7+ installed.
2. Check that you have the latest version of pip.
3. Try installing with the `--user` flag:

```bash
pip install --user darrell
```

If you still encounter issues, please check the Darrell GitHub repository for known installation problems or open a new issue with details about your system and the error message you're receiving.

Remember, if you encounter any issues not covered in this guide, don't hesitate to seek help from the Darrell community or consult the project's documentation for more detailed information.