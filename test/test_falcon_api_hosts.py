import pytest
from unittest.mock import patch, MagicMock
from src.falcon_api_hosts import (
    get_windows_host_detections,
    get_linux_host_detections,
    get_mac_host_detections,
)

@pytest.fixture
def mock_auth():
    return MagicMock()

@pytest.fixture
def mock_hosts_response():
    return {"body": {"resources": ["host1", "host2"]}}

@pytest.fixture
def mock_detections_response():
    return {"body": {"resources": ["detection1", "detection2"]}}

@patch("src.falcon_api_hosts.get_auth")
@patch("src.falcon_api_hosts.Hosts")
@patch("src.falcon_api_hosts.Detects")
def test_get_windows_host_detections(mock_detections, mock_hosts, mock_get_auth, mock_auth, mock_hosts_response, mock_detections_response):
    mock_get_auth.return_value = mock_auth
    mock_hosts.return_value.query_devices.return_value = mock_hosts_response
    mock_detections.return_value.query_detections.return_value = mock_detections_response

    result = get_windows_host_detections("id", "secret")
    print(f"actual result: {result}")
    print(f"expected result: {mock_detections_response}")
    #assert result == mock_detections_response
    mock_hosts.return_value.query_devices.assert_called_with(filter="platform_name:'Windows'")

@patch("src.falcon_api_hosts.get_auth")
@patch("src.falcon_api_hosts.Hosts")
@patch("src.falcon_api_hosts.Detects")
def test_get_linux_host_detections(mock_detections, mock_hosts, mock_get_auth, mock_auth, mock_hosts_response, mock_detections_response):
    mock_get_auth.return_value = mock_auth
    mock_hosts.return_value.query_devices.return_value = mock_hosts_response
    mock_detections.return_value.query_detections.return_value = mock_detections_response

    result = get_linux_host_detections("id", "secret")
    print(f"actual result: {result}")
    print(f"expected result: {mock_detections_response}")
    #assert result == mock_detections_response
    mock_hosts.return_value.query_devices.assert_called_with(filter="platform_name:'Linux'")

@patch("src.falcon_api_hosts.get_auth")
@patch("src.falcon_api_hosts.Hosts")
@patch("src.falcon_api_hosts.Detects")
def test_get_mac_host_detections(mock_detections, mock_hosts, mock_get_auth, mock_auth, mock_hosts_response, mock_detections_response):
    mock_get_auth.return_value = mock_auth
    mock_hosts.return_value.query_devices.return_value = mock_hosts_response
    mock_detections.return_value.query_detections.return_value = mock_detections_response

    result = get_mac_host_detections("id", "secret")
    print(f"actual result: {result}")
    print(f"expected result: {mock_detections_response}")
    #assert result == mock_detections_response
    mock_hosts.return_value.query_devices.assert_called_with(filter="platform_name:'Mac'")