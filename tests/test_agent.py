import json
import pytest
from agent.agent_code import run_agent

with open("cases_file/cases.json") as f:   # was: case_file/
    cases = json.load(f)

@pytest.mark.parametrize("case", cases, ids=[c["prompt"] for c in cases])
def test_agent_case(case):
    output = run_agent(case["prompt"])              # was: case["input"]
    assert case["expected_keyword"].lower() in output.lower()  # was: case["expected"]