def run_agent(prompt: str):

    prompt = prompt.lower()

    if "ai" in prompt:
        return "AI is the simulation of human intelligence by machines."

    if "neural network" in prompt:
        return "Neural networks are models inspired by the human brain."

    if "reinforcement" in prompt:
        return "Reinforcement learning learns through rewards."
    if "turing test" in prompt:
        return "The Turing Test evaluates a machine's ability to exhibit human-like intelligence."
    if "machine learning" in prompt:
        return "Machine learning is a subset of AI that enables systems to learn from data."
    return "I do not know."