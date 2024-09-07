from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dar",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Darrell Analytics Runner: dbt and Evidence BI orchestrator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dar",
    packages=find_packages(),
    install_requires=[
        "click",
        "dbt-core",
        "dbt-duckdb",
    ],
    entry_points={
        "console_scripts": [
            "dar=dar.cli:cli",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
