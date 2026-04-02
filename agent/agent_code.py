import re

def run_agent(prompt: str):
    prompt = prompt.lower()

    def contains(word):
        return bool(re.search(rf'\b{word}\b', prompt))

    if contains("neural network") or contains("neural networks"):
        return "Neural networks are models inspired by the human brain."
    if contains("reinforcement"):
        return "Reinforcement learning learns through rewards."
    if contains("turing test"):
        return "The Turing Test evaluates a machine's ability to exhibit human-like intelligence."
    if contains("machine learning"):
        return "Machine learning is a subset of AI that enables systems to learn from data."
    if contains("ai"):
        return "AI is the simulation of human intelligence by machines."

    return "I do not know."