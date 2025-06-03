from falconpy import FirewallPolicies
from src.falcon_api_firewall_policies import (
    get_falcon_api_credentials_from_aws,
    list_policies,
    create_linux_ssh_block_policy,
    delete_policy,
)

def test_create_and_delete_linux_policy():
    client_id, client_secret = get_falcon_api_credentials_from_aws()
    firewall = FirewallPolicies(client_id=client_id, client_secret=client_secret)

    # Create policy
    new_id = create_linux_ssh_block_policy(firewall)
    assert new_id is not None

    # Verify policy is in the list
    policy_ids = list_policies(firewall)
    assert new_id in policy_ids

    # Delete policy
    delete_policy(firewall, new_id)
    policy_ids_after = list_policies(firewall)
    assert new_id not in policy_ids_after