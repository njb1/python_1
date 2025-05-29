
crowdstrike_teams = ["engineering", "security", "threat-hunting", "threat-intelligence", "red-team", "blue-team", "purple-team"]
some_other_teams = []

def get_crowdstrike_teams():
    return crowdstrike_teams


def print_crowdstrike_teams(teams):
    for team in teams:
        print(team)

def add_crowdstrike_team(team):
    if team not in crowdstrike_teams:
        crowdstrike_teams.append(team)
        print(f"Team '{team}' added to CrowdStrike teams.")
        return
    else:
        print(f"Team '{team}' already exists in CrowdStrike teams.")


def remove_crowdstrike_team(team):
    if team in crowdstrike_teams:
        crowdstrike_teams.remove(team)
        print(f"Team '{team}' removed from CrowdStrike teams.")
    else:
        print(f"Team '{team}' not found in CrowdStrike teams.")


def sort_crowdstrike_teams():
    sorted_teams = sorted(crowdstrike_teams)
    print(f"Sorted CrowdStrike teams: {sorted_teams}")
    return sorted_teams


def make_copy_of_crowdstrike_teams():
    some_other_teams = crowdstrike_teams.copy()
    print(f"Copy of CrowdStrike teams created: {some_other_teams}")
    return some_other_teams

if __name__ == "__main__":
    teams = get_crowdstrike_teams()
    print(f"CrowdStrike Teams: {teams}")
    teams = add_crowdstrike_team("new-team")
    teams = get_crowdstrike_teams()
    print(f"CrowdStrike Teams after addition: {teams}")
    teams = remove_crowdstrike_team("new-team")
    teams = get_crowdstrike_teams()
    print(f"CrowdStrike Teams after removal: {teams}")
