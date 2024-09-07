from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Darrell",
    version="0.1.0",
    author="Chris Davis",
    author_email="chris@bootstrapital.com",
    description="Darrell - Open Source Analytics Stack",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bootstrapital/darrell",
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
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
)
