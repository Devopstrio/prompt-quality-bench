from setuptools import setup, find_packages

setup(
    name="prompt-quality-bench",
    version="1.0.0",
    description="Enterprise Prompt Engineering Benchmark & Quality Assessment CLI Utility",
    author="Devopstrio",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.0",
        "pydantic>=2.5.0",
        "httpx>=0.26.0",
        "pyyaml>=6.0.1",
        "tabulate>=0.9.0",
        "structlog>=24.1.0"
    ],
    entry_points={
        "console_scripts": [
            "pqbench=pqbench.cli.main:cli"
        ]
    },
    python_requires=">=3.9",
)
