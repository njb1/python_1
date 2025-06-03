from falconpy import OAuth2, FirewallPolicies
import boto3
import json


def get_falcon_api_credentials_from_aws():
    """
    Retrieve Falcon API credentials from AWS Secrets Manager (making a guess thats whats used).
    Expects a secret named 'falcon_secret' with keys 'client_id' and 'client_secret'.
    """
    secret_name = "falcon_secret"
    region_name = "us-east-1"  # Change to your region

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response["SecretString"]
        secret_dict = json.loads(secret)
        print("Retrieved Falcon API credentials from AWS Secrets Manager.")
        print(f"The whole body of the secret is: {secret_dict}") # Debugging line, get rid of it before pushing to production
        return secret_dict["client_id"], secret_dict["client_secret"]
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise


def get_auth(client_id, client_secret):
    return OAuth2(client_id=client_id, client_secret=client_secret)


def list_policies(firewall):
    print("=== Existing Policies ===")
    response = firewall.query_policies(limit=100)
    print(f"Status code: {response['status_code']}")
    print(f"Response body: {response['body']}")
    policy_ids = response["body"]["resources"]
    print(f"Found {len(policy_ids)} policies")
    return policy_ids


def create_linux_ssh_block_policy(firewall):
    linux_policy = {
        "resources": [
            {
                "name": "Block SSH Bruteforce",
                "platform_name": "Linux",
                "enabled": True,
                "description": "Limit SSH connections",
                "rules": [
                    {
                        "action": "BLOCK", # Or allow or probably continue inspection
                        "description": "Limit SSH connections",
                        "direction": "IN",
                        "protocol": "TCP",
                        "local_port": "22",
                        "remote_address": "any",
                        "frequency": "5/minute"  # Rate limiting
                    }
                ]
            }
        ]
    }
    create_resp = firewall.create_policies(body=linux_policy)
    new_id = create_resp["body"]["resources"][0]["id"]
    print(f"Created policy {new_id}")
    return new_id


def create_windows_ssh_block_policy(firewall):
    windows_policy = {
        "resources": [
            {
                "name": "Block SSH Bruteforce",
                "platform_name": "Windows",
                "enabled": True,
                "description": "Limit SSH connections",
                "rules": [
                    {
                        "action": "BLOCK", # Or allow or probably continue inspection
                        "description": "Limit SSH connections",
                        "direction": "IN",
                        "protocol": "TCP",
                        "local_port": "22",
                        "remote_address": "any",
                        "frequency": "5/minute"  # Rate limiting
                    }
                ]
            }
        ]
    }
    create_resp = firewall.create_policies(body=windows_policy)
    new_id = create_resp["body"]["resources"][0]["id"]
    print(f"Created Windows policy {new_id}")
    return new_id


def verify_policies(firewall):
    response = firewall.query_policies(limit=100)
    policy_ids = response["body"]["resources"]
    print(f"Total policies after creation: {len(policy_ids)}")
    print(f"Status code: {response['status_code']}")
    print(f"Response body: {response['body']}")
    return policy_ids


def delete_policy(firewall, policy_id):
    response = firewall.delete_policies(ids=[policy_id])
    print(f"Deleted policy {policy_id}")
    print(f"Status code: {response['status_code']}")
    print(f"Response body: {response['body']}")
    return response


def update_linux_ssh_block_policy(firewall, policy_id, new_description=None, new_name=None):
    """
    Update a Linux SSH block policy by ID.
    """
    update_body = {
        "resources": [
            {
                "id": policy_id,
                "platform_name": "Linux"
            }
        ]
    }
    if new_description:
        update_body["resources"][0]["description"] = new_description
    if new_name:
        update_body["resources"][0]["name"] = new_name

    response = firewall.update_policies(body=update_body)
    print(f"Updated Linux policy {policy_id}")
    print(f"Status code: {response['status_code']}")
    print(f"Response body: {response['body']}")
    return response


def update_windows_ssh_block_policy(firewall, policy_id, new_description=None, new_name=None):
    """
    Update a Windows SSH block policy by ID.
    """
    update_body = {
        "resources": [
            {
                "id": policy_id,
                "platform_name": "Windows"
            }
        ]
    }
    if new_description:
        update_body["resources"][0]["description"] = new_description
    if new_name:
        update_body["resources"][0]["name"] = new_name

    response = firewall.update_policies(body=update_body)
    print(f"Updated Windows policy {policy_id}")
    print(f"Status code: {response['status_code']}")
    print(f"Response body: {response['body']}")
    return response


if __name__ == "__main__":
    client_id, client_secret = get_falcon_api_credentials_from_aws()
    # I prefer this but its not best practie
    #client_id = get_falcon_api_credentials_from_aws()[0]
    #client_secret = get_falcon_api_credentials_from_aws()[1]
    auth = get_auth(client_id, client_secret)
    firewall = FirewallPolicies(auth)

    # List all policies
    list_policies(firewall)

    # Create a Linux policy to block SSH brute force
    new_id = create_linux_ssh_block_policy(firewall)

    # Verify
    verify_policies(firewall)

    # Update the description of a Linux policy
    update_linux_ssh_block_policy(firewall, policy_id="YOUR_POLICY_ID", new_description="New description for Linux policy")

    # Update the name of a Windows policy
    update_windows_ssh_block_policy(firewall, policy_id="YOUR_POLICY_ID", new_name="New Windows SSH Policy Name")

    # Cleanup (uncomment to enable deletion)
    # delete_policy(firewall, new_id)