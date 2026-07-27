import json
from pathlib import Path
from pqbench.mutators.prompt_mutator import PromptMutator
from pqbench.metrics.quality_scorer import PromptQualityScorer
from pqbench.reporting.report_generator import BenchmarkReportGenerator

def execute_suite():
    dataset_path = Path(__file__).parent / "sample_prompts.json"
    with open(dataset_path, "r", encoding="utf-8") as f:
        prompts = json.load(f)

    mutator = PromptMutator()
    scorer = PromptQualityScorer()
    reporter = BenchmarkReportGenerator()

    for item in prompts:
        print(f"\n=======================================================")
        print(f" Category: {item['category']} (ID: {item['id']})")
        print(f"=======================================================")
        mutations = mutator.generate_mutations(item["prompt"])
        evaluated = []

        for mut in mutations:
            scores = scorer.score_prompt(mut["prompt"])
            evaluated.append({
                "variant": mut["variant"],
                "prompt_text": mut["prompt"],
                "metrics": scores
            })

        print(reporter.generate_terminal_table(evaluated))

if __name__ == "__main__":
    execute_suite()
