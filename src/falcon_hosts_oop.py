import boto3
import json
from falconpy import OAuth2
from falconpy.hosts import Hosts
from falconpy.detects import Detects

my_fake_list_of_ids = ["some-host-id-1", "some-host-id-2", "some-host-id-3"]
my_fake_dict_of_ids = {"hostname1": "some-host-id-1", "hostname2": "some-host-id-2", "hostname3": "some-host-id-3"}


def get_falcon_api_credentials_from_aws():
    """
    Retrieve Falcon API credentials from AWS Secrets Manager.
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
        # print(f"The whole body of the secret is: {secret_dict}") # Remove or comment out for production
        return secret_dict["client_id"], secret_dict["client_secret"]
    except Exception as e:
        print(f"Error retrieving secret: {e}")
        raise


class FalconHost:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth = self.get_auth()

    def get_auth(self):
        return OAuth2(client_id=self.client_id, client_secret=self.client_secret)

    def get_host_detections(self, platform_name):
        hosts = Hosts(self.auth)
        hosts_response = hosts.query_devices_by_filter(filter=f"platform_name:'{platform_name}'")
        host_ids = hosts_response["body"]["resources"]
        detections = Detects(self.auth)
        detections_response = detections.query_detects(
            filter=f"device.device_id:['{','.join(host_ids)}']"
        )
        print(f"Found {len(detections_response['body']['resources'])} detections for {platform_name}.")
        return detections_response

    def get_windows_host_detections(self):
        return self.get_host_detections("Windows")

    def get_linux_host_detections(self):
        return self.get_host_detections("Linux")

    def get_mac_host_detections(self):
        return self.get_host_detections("Mac")
    
    def get_online_state(self, id_list):
        hosts = Hosts(self.auth)
        response = hosts.get_online_state(ids=id_list)
        print(response)
        return response
    
    def get_online_state_from_dict(self, my_fake_dict_of_ids):
        # Convert the dictionary to a list of IDs
        id_list = list(my_fake_dict_of_ids.keys())
        return self.get_online_state(id_list)

    def set_client_id(self, new_client_id):
        self.client_id = new_client_id

    def set_client_secret(self, new_client_secret):
        self.client_secret = new_client_secret

    def set_auth(self, new_auth):
        self.auth = new_auth

    def print_auth(self):
        # Print the authentication object for debugging or logging purposes
        print(f"Auth Object: {self.auth}")

    def print_client_id(self):
        # Print the client ID for debugging or logging purposes
        print(f"Client ID: {self.client_id}")

    def print_client_secret(self):
        # Print the client secret for debugging or logging purposes
        # Note: Be super cautious with printing sensitive information like client secrets
        print(f"Client Secret: {self.client_secret}")

    def print_auth_details(self):
        # Print both client ID and client secret
        self.print_client_id()
        self.print_client_secret()
        self.print_auth()


if __name__ == "__main__":
    client_id, client_secret = get_falcon_api_credentials_from_aws()
    falcon_host = FalconHost(client_id, client_secret)
    falcon_host.get_windows_host_detections()
    falcon_host.get_online_state(my_fake_list_of_ids)