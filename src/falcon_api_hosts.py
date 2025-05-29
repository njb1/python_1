from falconpy import OAuth2, Hosts, Detects


def get_auth(client_id, client_secret):
    return OAuth2(client_id=client_id, client_secret=client_secret)


def get_windows_host_detections(client_id, client_secret):
    auth = get_auth(client_id, client_secret)
    hosts = Hosts(auth)
    hosts_response = hosts.query_devices_by_filter(filter="platform_name:'Windows'")
    host_ids = hosts_response["body"]["resources"]
    detections = Detects(auth)
    detections_response = detections.query_detects(
        filter=f"device.device_id:['{','.join(host_ids)}']"
    )
    print(f"Found {len(detections_response['body']['resources'])} detections.")
    return detections_response


def get_linux_host_detections(client_id, client_secret):
    auth = get_auth(client_id, client_secret)
    hosts = Hosts(auth)
    hosts_response = hosts.query_devices_by_filter(filter="platform_name:'Linux'")
    host_ids = hosts_response["body"]["resources"]
    detections = Detects(auth)
    detections_response = detections.query_detects(
        filter=f"device.device_id:['{','.join(host_ids)}']"
    )
    print(f"Found {len(detections_response['body']['resources'])} detections.")
    return detections_response


def get_mac_host_detections(client_id, client_secret):
    auth = get_auth(client_id, client_secret)
    hosts = Hosts(auth)
    hosts_response = hosts.query_devices_by_filter(filter="platform_name:'Mac'")
    host_ids = hosts_response["body"]["resources"]
    detections = Detects(auth)
    detections_response = detections.query_detects(
        filter=f"device.device_id:['{','.join(host_ids)}']"
    )
    print(f"Found {len(detections_response['body']['resources'])} detections.")
    return detections_response


if __name__ == "__main__":
    pass
    #get_windows_host_detections("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")
    #get_linux_host_detections("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")
    #get_linux_host_detections("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")