from falconpy import UserManagement
from falcon_api_firewall_policies import get_falcon_api_credentials_from_aws

def create_user(user_mgmt, first_name, last_name, email):
    """
    Create a new user in Falcon.
    :param user_mgmt: An instance of the falconpy.UserManagement object (?)
    :param first_name: User's first name
    :param last_name: User's last name
    :param email: User's email address (used as username)
    """
    response = user_mgmt.create_user(
        first_name=first_name,
        last_name=last_name,
        uid=email
    )
    print(f"Create user response status: {response['status_code']}")
    print(f"Response body: {response['body']}")
    return response

def delete_user(user_mgmt, user_uuid):
    """
    Delete a user in Falcon by UUID.
    :param user_mgmt: An instance of falconpy.UserManagement
    :param user_uuid: The user's UUID
    """
    response = user_mgmt.delete_user(user_uuid=user_uuid)
    print(f"Delete user response status: {response['status_code']}")
    print(f"Response body: {response['body']}")
    return response

if __name__ == "__main__":
    # Replace with your actual CrowdStrike API credentials
    client_id, client_secret = get_falcon_api_credentials_from_aws()

    # Example user details
    first_name = "Neil"
    last_name = "Burns"
    email = "neil.burns@crowdstrike.com"

    user_mgmt = UserManagement(client_id=client_id, client_secret=client_secret)
    create_user(user_mgmt, first_name, last_name, email)

    # create_response = create_user(user_mgmt, first_name, last_name, email)
    # user_uuid = create_response["body"]["resources"][0]["user_uuid"]
    delete_user(user_mgmt, user_uuid="some-user-uuid")