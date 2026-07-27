from pqbench.metrics.quality_scorer import PromptQualityScorer

def test_quality_scorer():
    scorer = PromptQualityScorer()
    prompt = "You are a role expert. Return strictly valid JSON format step by step."
    scores = scorer.score_prompt(prompt)
    assert scores["specificity_score"] > 0.0
    assert scores["overall_quality_grade"] in ["A+", "B"]
