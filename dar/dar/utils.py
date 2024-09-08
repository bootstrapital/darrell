

def run_dbt_init(path):
    import pexpect
    
    child = pexpect.spawn('dbt init')
    
    # Define expected prompts and responses
    interactions = [
        ("Enter a name for your project", path),
        ("Enter a number", "1"),
    ]
    
    for prompt, response in interactions:
        child.expect(prompt)
        child.sendline(response)
    
    # Wait for the process to finish
    child.expect(pexpect.EOF)
    
    print("dbt project initialized successfully with DuckDB!")