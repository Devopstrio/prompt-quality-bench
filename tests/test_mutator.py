from pqbench.mutators.prompt_mutator import PromptMutator

def test_prompt_mutations_generation():
    mutator = PromptMutator()
    base = "Summarize the quarterly financial report."
    mutations = mutator.generate_mutations(base)
    assert len(mutations) == 4
    variants = [m["variant"] for m in mutations]
    assert "baseline" in variants
    assert "chain_of_thought" in variants
    assert "role_persona" in variants
