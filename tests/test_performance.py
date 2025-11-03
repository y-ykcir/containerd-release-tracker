"""Performance tests for concurrent fetching and caching."""

import pytest
from unittest.mock import Mock, patch
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.github_client import GitHubClient
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


@patch('requests.Session.get')
def test_get_prs_batch_concurrent(mock_get, github_client):
    """Test concurrent PR fetching."""
    # Mock response for PRs
    def mock_pr_response(url):
        pr_number = int(url.split('/')[-1])
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'number': pr_number,
            'title': f'PR {pr_number}',
            'html_url': f'https://github.com/test/repo/pull/{pr_number}',
            'body': 'Test body',
            'state': 'closed',
            'merged': True,
            'created_at': '2024-01-01T00:00:00Z',
            'merged_at': '2024-01-02T00:00:00Z',
            'user': {'login': 'test_author'},
            'labels': []
        }
        return mock_response
    
    mock_get.side_effect = lambda url, **kwargs: mock_pr_response(url)
    
    # Fetch multiple PRs
    pr_numbers = [1, 2, 3, 4, 5]
    results = github_client.get_prs_batch(pr_numbers)
    
    assert len(results) == 5
    for pr_num in pr_numbers:
        assert results[pr_num] is not None
        assert results[pr_num].number == pr_num


@patch('requests.Session.get')
def test_get_issues_batch_concurrent(mock_get, github_client):
    """Test concurrent issue fetching."""
    # Mock response for issues
    def mock_issue_response(url):
        issue_number = int(url.split('/')[-1])
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'number': issue_number,
            'title': f'Issue {issue_number}',
            'html_url': f'https://github.com/test/repo/issues/{issue_number}',
            'body': 'Test body',
            'state': 'closed',
            'created_at': '2024-01-01T00:00:00Z',
            'closed_at': '2024-01-02T00:00:00Z',
            'user': {'login': 'test_author'},
            'labels': []
        }
        return mock_response
    
    mock_get.side_effect = lambda url, **kwargs: mock_issue_response(url)
    
    # Fetch multiple issues
    issue_numbers = [1, 2, 3, 4, 5]
    results = github_client.get_issues_batch(issue_numbers)
    
    assert len(results) == 5
    for issue_num in issue_numbers:
        assert results[issue_num] is not None
        assert results[issue_num].number == issue_num


@patch('requests.Session.get')
def test_pr_caching(mock_get, github_client):
    """Test that PRs are cached and not refetched."""
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        'number': 123,
        'title': 'Test PR',
        'html_url': 'https://github.com/test/repo/pull/123',
        'body': 'Test body',
        'state': 'closed',
        'merged': True,
        'created_at': '2024-01-01T00:00:00Z',
        'merged_at': '2024-01-02T00:00:00Z',
        'user': {'login': 'test_author'},
        'labels': []
    }
    mock_get.return_value = mock_response
    
    # First fetch
    pr1 = github_client.get_pr_info(123)
    assert pr1 is not None
    assert mock_get.call_count == 1
    
    # Second fetch should use cache
    pr2 = github_client.get_pr_info(123)
    assert pr2 is not None
    assert pr2.number == pr1.number
    assert mock_get.call_count == 1  # Should still be 1, not 2


@patch('requests.Session.get')
def test_issue_caching(mock_get, github_client):
    """Test that issues are cached and not refetched."""
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        'number': 456,
        'title': 'Test Issue',
        'html_url': 'https://github.com/test/repo/issues/456',
        'body': 'Test body',
        'state': 'closed',
        'created_at': '2024-01-01T00:00:00Z',
        'closed_at': '2024-01-02T00:00:00Z',
        'user': {'login': 'test_author'},
        'labels': []
    }
    mock_get.return_value = mock_response
    
    # First fetch
    issue1 = github_client.get_issue_info(456)
    assert issue1 is not None
    assert mock_get.call_count == 1
    
    # Second fetch should use cache
    issue2 = github_client.get_issue_info(456)
    assert issue2 is not None
    assert issue2.number == issue1.number
    assert mock_get.call_count == 1  # Should still be 1, not 2


@patch('requests.Session.get')
def test_batch_uses_cache(mock_get, github_client):
    """Test that batch fetching uses cache for already fetched items."""
    def mock_response(url):
        pr_number = int(url.split('/')[-1])
        mock_resp = Mock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {
            'number': pr_number,
            'title': f'PR {pr_number}',
            'html_url': f'https://github.com/test/repo/pull/{pr_number}',
            'body': 'Test body',
            'state': 'closed',
            'merged': True,
            'created_at': '2024-01-01T00:00:00Z',
            'merged_at': '2024-01-02T00:00:00Z',
            'user': {'login': 'test_author'},
            'labels': []
        }
        return mock_resp
    
    mock_get.side_effect = lambda url, **kwargs: mock_response(url)
    
    # Fetch PR 1 individually
    pr1 = github_client.get_pr_info(1)
    assert pr1 is not None
    call_count_after_first = mock_get.call_count
    
    # Batch fetch PRs 1, 2, 3 - PR 1 should use cache
    results = github_client.get_prs_batch([1, 2, 3])
    assert len(results) == 3
    # Should only have made 2 additional calls (for PRs 2 and 3)
    assert mock_get.call_count == call_count_after_first + 2


def test_regex_patterns_precompiled(github_client):
    """Test that regex patterns are compiled at class level."""
    # Verify that patterns exist as class attributes
    assert hasattr(GitHubClient, '_PR_PATTERNS')
    assert hasattr(GitHubClient, '_ISSUE_PATTERNS')
    assert hasattr(GitHubClient, '_CHERRY_PICK_PATTERNS')
    
    # Verify they are compiled patterns
    import re
    assert all(isinstance(p, re.Pattern) for p in GitHubClient._PR_PATTERNS)
    assert all(isinstance(p, re.Pattern) for p in GitHubClient._ISSUE_PATTERNS)
    assert all(isinstance(p, re.Pattern) for p in GitHubClient._CHERRY_PICK_PATTERNS)
