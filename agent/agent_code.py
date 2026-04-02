def run_agent(prompt: str):

    prompt = prompt.lower()

    if "ai" in prompt:
        return "AI is the simulation of human intelligence by machines."

    if "neural network" in prompt:
        return "Neural networks are models inspired by the human brain."

    if "reinforcement" in prompt:
        return "Reinforcement learning learns through rewards."

    return "I do not know."