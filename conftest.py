import pytest

from src.dict import (
    get_team_description,
    add_crowdstrike_team,
    remove_crowdstrike_team,
    update_team_description,
    get_all_team_names,
    get_all_team_descriptions,
    crowdstrike_teams_dict,
)

@pytest.fixture
def list_of_other_teams():
    return ["team1", "team2", "team3"]

@pytest.fixture(autouse=True)
def reset_dict():
    # Reset the dictionary before each test
    original = {
        "engineering": "Develops and maintains CrowdStrike products.",
        "security": "Ensures the security of CrowdStrike infrastructure.",
        "threat-hunting": "Proactively hunts for threats in customer environments.",
        "threat-intelligence": "Analyzes and reports on threat actors.",
        "red-team": "Simulates attacks to test defenses.",
        "blue-team": "Defends against attacks and responds to incidents.",
        "purple-team": "Facilitates collaboration between red and blue teams."
    }
    crowdstrike_teams_dict.clear()
    crowdstrike_teams_dict.update(original)
    yield
    crowdstrike_teams_dict.clear()
    crowdstrike_teams_dict.update(original)