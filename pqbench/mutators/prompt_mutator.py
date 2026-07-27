from typing import Dict, Any, List, Optional, Union

class PromptMutator:
    """
    Prompt Variant Mutator & Permutation Engine.
    Generates systematic prompt variations (System Persona Injection, Chain-of-Thought, Few-Shot Formatting).
    """

    def generate_mutations(self, base_prompt: str) -> List[Dict[str, str]]:
        mutations = [
            {
                "variant": "baseline",
                "prompt": base_prompt
            },
            {
                "variant": "chain_of_thought",
                "prompt": f"{base_prompt}\n\nLet's think step by step before answering."
            },
            {
                "variant": "role_persona",
                "prompt": f"You are a principal enterprise AI architect.\n\nTask: {base_prompt}"
            },
            {
                "variant": "json_format_guard",
                "prompt": f"{base_prompt}\n\nReturn your final output in strictly valid JSON format."
            }
        ]
        return mutations
