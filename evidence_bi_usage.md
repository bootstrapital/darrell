# Evidence BI Usage with Darrell

Darrell provides a seamless integration with Evidence BI, allowing you to build, preview, and update your reports efficiently. This guide will walk you through the process of using Darrell with Evidence BI.

## Building Reports

To generate static files for your Evidence reports, use the following command:

```
darrell reports build
```

This command changes to the `reports` directory and runs the `npm run build` command, which builds your Evidence project.

## Previewing Reports

To run the Evidence development server and preview your reports, use:

```
darrell reports preview
```

This command changes to the `reports` directory and runs `npm run dev`, starting the Evidence development server.

## Updating Sources

To update the sources for your Evidence reports, use:

```
darrell reports update
```

This command changes to the `reports` directory and runs `npm run sources`, which updates the sources for your Evidence project.

## Additional Notes

- The `refresh` command is currently a placeholder and does not perform any actions. In the future, it is intended to copy compiled dbt models to the Evidence source folder.

- All Evidence-related commands are executed from the `reports` directory, which is assumed to be your Evidence project root.

- Make sure you have npm and the necessary dependencies installed in your Evidence project before running these commands.

## Tips for Efficient Workflow

1. Use `darrell reports preview` during development to see live updates as you modify your reports.
2. Run `darrell reports update` whenever you need to refresh the data sources for your reports.
3. Once you're satisfied with your reports, use `darrell reports build` to generate the static files for deployment.

By leveraging these commands, you can streamline your workflow when working with Evidence BI in your Darrell-managed project.