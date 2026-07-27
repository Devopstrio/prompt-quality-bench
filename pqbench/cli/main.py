import click
import json
from typing import Dict, Any, List, Optional, Union

from pqbench.mutators.prompt_mutator import PromptMutator
from pqbench.metrics.quality_scorer import PromptQualityScorer
from pqbench.reporting.report_generator import BenchmarkReportGenerator

@click.group()
def cli():
    """
    pqbench: Enterprise Prompt Engineering Benchmark & Quality Assessment CLI Tool.
    """
    pass

@cli.command(name="run")
@click.option("--prompt", "-p", required=True, help="Base prompt text to benchmark.")
@click.option("--format", "-f", type=click.Choice(["table", "json"]), default="table", help="Output format.")
def run_benchmark(prompt: str, format: str):
    """
    Executes prompt mutation, metrics scoring, and outputs quality benchmark report.
    """
    mutator = PromptMutator()
    scorer = PromptQualityScorer()
    reporter = BenchmarkReportGenerator()

    mutations = mutator.generate_mutations(prompt)
    evaluated = []

    for mut in mutations:
        scores = scorer.score_prompt(mut["prompt"])
        evaluated.append({
            "variant": mut["variant"],
            "prompt_text": mut["prompt"],
            "metrics": scores
        })

    if format == "json":
        report = reporter.generate_json_report(evaluated)
        click.echo(json.dumps(report, indent=2))
    else:
        table_output = reporter.generate_terminal_table(evaluated)
        click.echo("\n--- Prompt Quality Benchmark Results ---\n")
        click.echo(table_output)
        click.echo("\n")

if __name__ == "__main__":
    cli()
