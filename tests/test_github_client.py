"""Tests for GitHub client module."""

import pytest
from unittest.mock import Mock, patch
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.github_client import GitHubClient, ReleaseInfo, PRInfo, IssueInfo
from src.config import GitHubConfig


@pytest.fixture
def github_config():
    """Create a test GitHub configuration."""
    return GitHubConfig(
        api_url="https://api.github.com",
        repo_owner="containerd",
        repo_name="containerd",
        token="test_token"
    )


@pytest.fixture
def github_client(github_config):
    """Create a test GitHub client."""
    return GitHubClient(github_config)


def test_extract_pr_numbers_from_text(github_client):
    """Test PR number extraction from text."""
    text = """
    This release includes:
    - Fix for #12345
    - Update from https://github.com/containerd/containerd/pull/12346
    - Another fix #12347
    """
    
    pr_numbers = github_client.extract_pr_numbers_from_text(text)
    assert set(pr_numbers) == {12345, 12346, 12347}


def test_extract_issue_numbers_from_text(github_client):
    """Test issue number extraction from text."""
    text = """
    This PR fixes https://github.com/containerd/containerd/issues/12345
    Also resolves #12346
    Closes #12347
    """
    
    issue_numbers = github_client.extract_issue_numbers_from_text(text)
    assert set(issue_numbers) == {12345, 12346, 12347}


@patch('requests.Session.get')
def test_get_latest_release_success(mock_get, github_client):
    """Test successful latest release retrieval."""
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        'tag_name': 'v2.1.4',
        'name': 'containerd 2.1.4',
        'body': 'Release notes...',
        'published_at': '2024-01-01T00:00:00Z',
        'prerelease': False,
        'draft': False,
        'html_url': 'https://github.com/containerd/containerd/releases/tag/v2.1.4',
        'author': {'login': 'test_author'}
    }
    mock_get.return_value = mock_response
    
    release = github_client.get_latest_release()
    
    assert release is not None
    assert release.tag_name == 'v2.1.4'
    assert release.name == 'containerd 2.1.4'
    assert release.author == 'test_author'


@patch('requests.Session.get')
def test_get_latest_release_failure(mock_get, github_client):
    """Test failed latest release retrieval."""
    import requests
    mock_get.side_effect = requests.RequestException("API Error")

    release = github_client.get_latest_release()

    assert release is None


@patch('requests.Session.get')
def test_get_pr_info_success(mock_get, github_client):
    """Test successful PR info retrieval."""
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        'number': 12345,
        'title': 'Fix important bug',
        'html_url': 'https://github.com/containerd/containerd/pull/12345',
        'body': 'This fixes a critical issue',
        'state': 'closed',
        'merged': True,
        'created_at': '2024-01-01T00:00:00Z',
        'merged_at': '2024-01-02T00:00:00Z',
        'user': {'login': 'test_author'},
        'labels': [{'name': 'bug'}, {'name': 'critical'}]
    }
    mock_get.return_value = mock_response
    
    pr_info = github_client.get_pr_info(12345)
    
    assert pr_info is not None
    assert pr_info.number == 12345
    assert pr_info.title == 'Fix important bug'
    assert pr_info.merged is True
    assert pr_info.labels == ['bug', 'critical']
