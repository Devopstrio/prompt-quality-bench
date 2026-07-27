from typing import Dict, Any, List, Optional, Union

class PromptQualityScorer:
    """
    Prompt Quality & Complexity Metric Evaluator.
    Calculates token efficiency, specificity score, and structural clarity index.
    """

    def score_prompt(self, prompt_text: str) -> Dict[str, Any]:
        words = prompt_text.split()
        word_count = len(words)
        char_count = len(prompt_text)

        # Calculate specificity score based on structural keywords
        keywords = ["json", "step", "role", "must", "strictly", "format", "schema"]
        matches = sum(1 for kw in keywords if kw in prompt_text.lower())
        specificity_score = min(1.0, round(matches / 4.0, 2))

        # Structural clarity score
        clarity_score = 0.9 if "\n" in prompt_text else 0.6

        return {
            "word_count": word_count,
            "char_count": char_count,
            "specificity_score": specificity_score,
            "clarity_score": clarity_score,
            "overall_quality_grade": "A+" if (specificity_score >= 0.5 and clarity_score >= 0.8) else "B"
        }
