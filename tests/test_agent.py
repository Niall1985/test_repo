# tests/test_agent.py

import json
import pytest
from pathlib import Path
from agent.agent_code import run_agent

# __file__ is tests/test_agent.py
# .parent      is tests/
# .parent.parent is the repo root  ← cases_file/ lives here
CASES_PATH = Path(__file__).parent.parent / "cases_file" / "cases.json"

with open(CASES_PATH) as f:
    cases = json.load(f)

@pytest.mark.parametrize("case", cases, ids=[c["prompt"] for c in cases])
def test_agent_case(case):
    output = run_agent(case["prompt"])
    assert case["expected_keyword"].lower() in output.lower()