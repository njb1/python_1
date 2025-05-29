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


def test_get_team_description_existing():
    assert get_team_description("engineering") == "Develops and maintains CrowdStrike products."

def test_get_team_description_nonexistent():
    assert get_team_description("devops") == "Team not found."

def test_add_crowdstrike_team():
    add_crowdstrike_team("devops", "Handles deployment pipelines and cloud ops.")
    assert "devops" in crowdstrike_teams_dict
    assert crowdstrike_teams_dict["devops"] == "Handles deployment pipelines and cloud ops."

def test_add_existing_team_does_not_overwrite():
    add_crowdstrike_team("engineering", "Should not overwrite.")
    assert crowdstrike_teams_dict["engineering"] == "Develops and maintains CrowdStrike products."

def test_remove_crowdstrike_team():
    add_crowdstrike_team("devops", "Handles deployment pipelines and cloud ops.")
    remove_crowdstrike_team("devops")
    assert "devops" not in crowdstrike_teams_dict

def test_remove_nonexistent_team():
    remove_crowdstrike_team("nonexistent")  # Should not raise

def test_update_team_description():
    update_team_description("engineering", "New description.")
    assert crowdstrike_teams_dict["engineering"] == "New description."

def test_update_nonexistent_team():
    update_team_description("devops", "Should not add.")
    assert "devops" not in crowdstrike_teams_dict

def test_get_all_team_names():
    names = get_all_team_names()
    assert set(names) == set([
        "engineering", "security", "threat-hunting", "threat-intelligence",
        "red-team", "blue-team", "purple-team"
    ])

# def test_get_all_team_descriptions():
#     descriptions = get_all_team_descriptions()
#     for desc in [
#         "Develops and maintains CrowdStrike products.",
#         "Ensures the security of CrowdStrike infrastructure.",
#         "Proactively hunts for threats in customer environments.",
#         "Analyzes and reports on threat actors.",
#         "Simulates attacks to test defenses.",
#         "Defends against attacks and responds to incidents.",
#         "Facilitates collaboration between red and blue teams."
#     ]:
#         assert desc in descriptions