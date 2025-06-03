import requests

def create_firewall_policy_crowdstrike(api_token, policy_body):
    """
    Creates a new firewall policy in CrowdStrike using the CrowdStrike API.
    """
    url = "https://crowdstrike.com/policy/entities/firewall/v1"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=policy_body)
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")
    return response

if __name__ == "__main__":
    fake_token = "FAKE_TOKEN"
    fake_body = {
        "resources": [
            {
                "clone_id": "example-clone-id",
                "description": "Example policy for testing",
                "name": "Test Policy",
                "platform_name": "Windows"
            }
        ]
    }
    create_firewall_policy_crowdstrike(fake_token, fake_body)