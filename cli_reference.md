# Darrell CLI Reference

This page provides a comprehensive reference of all CLI commands available in Darrell, including their purpose, parameters, and example usage. The commands are organized by category: dbt, Evidence, and site.

## Main CLI

The main Darrell CLI is accessed through the `dar` command.

```bash
dar [OPTIONS] COMMAND [ARGS]...
```

**Description:** Orchestrating dbt and Evidence BI for an Open Source Analytics Stack

### Global Commands

#### `dar setup`

Initialize a new Darrell project.

```bash
dar setup
```

## dbt Commands

dbt commands are accessed through `dar models`.

### `dar models init`

Initialize a new dbt project.

```bash
dar models init
```

### `dar models run`

Run dbt models.

```bash
dar models run [OPTIONS]
```

**Options:**
- `-s, --select TEXT`: Specify models to run

**Example:**
```bash
dar models run -s my_model
```

### `dar models test`

Run dbt tests.

```bash
dar models test [OPTIONS]
```

**Options:**
- `-s, --select TEXT`: Specify models to test

**Example:**
```bash
dar models test -s my_model
```

### `dar models docs`

Generate dbt documentation.

```bash
dar models docs
```

### `dar models compile`

Compile dbt models.

```bash
dar models compile
```

## Evidence Commands

Evidence commands are accessed through `dar reports`.

### `dar reports build`

Generate Evidence static files.

```bash
dar reports build
```

### `dar reports preview`

Run Evidence dev server.

```bash
dar reports preview
```

### `dar reports refresh`

Copy dbt models to Evidence (currently not implemented).

```bash
dar reports refresh
```

### `dar reports update`

Run Evidence sources.

```bash
dar reports update
```

## Site Commands

Site commands are accessed through `dar site`, but currently, no specific commands are implemented in the provided code.