import json
from agent.agent_code import run_agent


with open("case_file/cases.json") as f:
    cases = json.load(f)


def test_cases():

    for case in cases:

        output = run_agent(case["input"])

        assert case["expected"].lower() in output.lower()