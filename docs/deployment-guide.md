# Developer & CLI Usage Guide: Prompt Quality Bench (`pqbench`)

This guide covers local installation, CLI usage, prompt suite execution, and pytest testing.

## 1. Installation

```bash
# Clone repository
git clone https://github.com/Devopstrio/prompt-quality-bench.git
cd prompt-quality-bench

# Install CLI executable globally or in venv
pip install -e .
```

## 2. CLI Usage Examples

```bash
# Run benchmark on a prompt (Table output)
pqbench run --prompt "Summarize cloud security architecture standards."

# Run benchmark with JSON output format
pqbench run --prompt "Write a Python script for S3 bucket encryption." --format json
```

## 3. Execute Batch Benchmark Dataset Suite

```bash
python benchmarks/run_benchmark_suite.py
```

## 4. Running Pytest Test Suite

```bash
python -m pytest -v tests/
```
