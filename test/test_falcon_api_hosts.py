import pytest
from unittest.mock import patch, MagicMock
from src.falcon_api_hosts import (
    get_windows_host_detections,
    get_linux_host_detections,
    get_mac_host_detections,
)
from src.falcon_api_firewall_policies import get_falcon_api_credentials_from_aws


def test_get_windows_host_detections():
    client_id, client_secret = get_falcon_api_credentials_from_aws()
    response = get_windows_host_detections(client_id, client_secret)
    assert "body" in response
    assert "resources" in response["body"]
    #assert isinstance(response["body"]["resources"], list)

def test_get_linux_host_detections():
    client_id, client_secret = get_falcon_api_credentials_from_aws()
    response = get_linux_host_detections(client_id, client_secret)
    assert "body" in response
    assert "resources" in response["body"]
    #assert isinstance(response["body"]["resources"], list)

def test_get_mac_host_detections():
    client_id, client_secret = get_falcon_api_credentials_from_aws()
    response = get_mac_host_detections(client_id, client_secret)
    assert "body" in response
    assert "resources" in response["body"]
    #assert isinstance(response["body"]["resources"], list)