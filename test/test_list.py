from src.lists import (
    add_crowdstrike_team,
    remove_crowdstrike_team,   
    make_copy_of_crowdstrike_teams,
    sort_crowdstrike_teams,
    crowdstrike_teams,
)
import pytest
from conftest import list_of_other_teams

def test_sort_crowdstrike_teams():
    sorted_list = sort_crowdstrike_teams()
    assert sorted_list == sorted(crowdstrike_teams)
    print(f"Sorted list: {sorted_list}")
    print(f"Original list: {crowdstrike_teams}")
    assert sorted_list != crowdstrike_teams
    print(f"Original list after sorting: {crowdstrike_teams}")
    print(f"Sorted list: {sorted_list}")


def test_add_crowdstrike_team(list_of_other_teams):
    for team in list_of_other_teams:
        add_crowdstrike_team(team)
        assert team in crowdstrike_teams
        print(f"Team '{team}' added to the list")



def test_remove_crowdstrike_team(list_of_other_teams):
    for team in list_of_other_teams:
        remove_crowdstrike_team(team)
        assert team not in crowdstrike_teams
        print(f"Team '{team}' removed from the list")


def test_make_copy_of_crowdstrike_teams():
    copy_of_teams = make_copy_of_crowdstrike_teams()
    assert copy_of_teams == crowdstrike_teams, "The copied list does not match the original"
    print(f"Copy of teams: {copy_of_teams}")
    assert copy_of_teams is not crowdstrike_teams, "The copied list should not be the same object as the original"
    print(f"Original list: {crowdstrike_teams}")