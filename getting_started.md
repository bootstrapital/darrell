# Getting Started with Darrell

Darrell is an open-source analytics stack designed for nimble data teams, wrapping dbt and Evidence BI into a single, easy-to-use package. This guide will help you get started with Darrell, covering installation, basic usage, and an overview of its main features.

## Installation

To install Darrell, you'll need Python 3.9 or higher. Follow these steps to get started:

1. Open your terminal or command prompt.
2. Run the following command to install Darrell using pip:

```bash
pip install Darrell
```

This command will install Darrell and its dependencies, including dbt-core and dbt-duckdb.

## Basic Usage

After installation, you can start using Darrell through its command-line interface (CLI). Here are some basic commands to get you started:

### 1. Set up a new Darrell project

To set up a new Darrell project, use the following command:

```bash
dar setup
```

This command will guide you through the initial setup process for your Darrell project.

### 2. Working with dbt models

Darrell uses dbt for data modeling. You can interact with dbt models using the `models` subcommand:

```bash
dar models [dbt-command]
```

For example, to run your dbt models:

```bash
dar models run
```

### 3. Creating and managing reports

Darrell integrates with Evidence BI for reporting. Use the `reports` subcommand to work with Evidence BI:

```bash
dar reports [evidence-command]
```

## Main Features

Darrell combines the power of dbt and Evidence BI to provide a comprehensive analytics stack. Here's an overview of its main features:

1. **Unified CLI**: Darrell provides a single command-line interface to manage both dbt models and Evidence BI reports.

2. **dbt Integration**: Leverage dbt's powerful data transformation and modeling capabilities directly through Darrell.

3. **Evidence BI Integration**: Create and manage reports using Evidence BI, all within the Darrell ecosystem.

4. **Easy Setup**: The `dar setup` command simplifies the process of setting up your analytics environment.

5. **Extensibility**: As an open-source project, Darrell can be extended and customized to fit your team's specific needs.

## Next Steps

Now that you've got Darrell installed and understand its basic usage, you can start building your analytics stack. Here are some suggestions for next steps:

1. Explore the `dar models` commands to start creating and managing your dbt models.
2. Use `dar reports` to begin working with Evidence BI and create your first reports.
3. Check out the Darrell GitHub repository at https://github.com/bootstrapital/darrell for more advanced usage and contribution guidelines.

Remember, Darrell is designed to make your analytics workflow more efficient and integrated. As you become more familiar with its features, you'll be able to leverage its full potential to streamline your data team's work.