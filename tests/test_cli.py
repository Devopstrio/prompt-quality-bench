from click.testing import CliRunner
from pqbench.cli.main import cli

def test_cli_run_command_table():
    runner = CliRunner()
    result = runner.invoke(cli, ["run", "--prompt", "Explain cloud architecture."])
    assert result.exit_code == 0
    assert "Prompt Quality Benchmark Results" in result.output

def test_cli_run_command_json():
    runner = CliRunner()
    result = runner.invoke(cli, ["run", "--prompt", "Explain AI models.", "--format", "json"])
    assert result.exit_code == 0
    assert "total_variants_evaluated" in result.output
