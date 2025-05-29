# Example CrowdStrike dictionary: team name -> team description
crowdstrike_teams_dict = {
    "engineering": "Develops and maintains CrowdStrike products.",
    "security": "Ensures the security of CrowdStrike infrastructure.",
    "threat-hunting": "Proactively hunts for threats in customer environments.",
    "threat-intelligence": "Analyzes and reports on threat actors.",
    "red-team": "Simulates attacks to test defenses.",
    "blue-team": "Defends against attacks and responds to incidents.",
    "purple-team": "Facilitates collaboration between red and blue teams."
}

def get_team_description(team_name):
    """
    Return the description for a given team.
    """
    return crowdstrike_teams_dict.get(team_name, "Team not found.")

def add_crowdstrike_team(team_name, description):
    """
    Add a new team to the dictionary.
    """
    if team_name in crowdstrike_teams_dict:
        print(f"Team '{team_name}' already exists.")
    else:
        crowdstrike_teams_dict[team_name] = description
        print(f"Team '{team_name}' added.")

def remove_crowdstrike_team(team_name):
    """
    Remove a team from the dictionary.
    """
    if team_name in crowdstrike_teams_dict:
        del crowdstrike_teams_dict[team_name]
        print(f"Team '{team_name}' removed.")
    else:
        print(f"Team '{team_name}' not found.")

def list_all_teams():
    """
    Print all teams and their descriptions.
    """
    for team, desc in crowdstrike_teams_dict.items():
        print(f"{team}: {desc}")

def update_team_description(team_name, new_description):
    """
    Update the description for a given team.
    """
    if team_name in crowdstrike_teams_dict:
        crowdstrike_teams_dict[team_name] = new_description
        print(f"Description for '{team_name}' updated.")
    else:
        print(f"Team '{team_name}' not found.")

def get_all_team_names():
    """
    Return a list of all team names.
    """
    return list(crowdstrike_teams_dict.keys())

def get_all_team_descriptions():
    """
    Return a list of all team descriptions.
    """
    return list(crowdstrike_teams_dict.values())

if __name__ == "__main__":
    list_all_teams()
    #add_crowdstrike_team("devops", "Manages CI/CD and cloud infrastructure.")
    #("devops", "Handles deployment pipelines and cloud ops.")
    #print(get_team_description("devops"))
    #remove_crowdstrike_team("devops")
    print(get_all_team_names())
    print(get_all_team_descriptions())