"""Tests for the dynamic logging configuration."""

from unittest.mock import mock_open, patch
import os
import pytest
from dyn_logging import update_logging_config

@pytest.mark.parametrize('log_level, log_file, expected_config', [
    ('INFO', 'logs/info.log', "level=INFO\nargs=('logs/info.log', 'a')"),
    ('WARNING', 'logs/warning.log', "level=WARNING\nargs=('logs/warning.log', 'a')"),
    ('ERROR', 'logs/error.log', "level=ERROR\nargs=('logs/error.log', 'a')"),
])
def test_update_logging_config(log_level, log_file, expected_config):
    """Test the update_logging_config function with various environment variables."""
    os.environ['LOG_LEVEL'] = log_level
    os.environ['LOG_FILE'] = log_file

    original_config = "level=DEBUG\nargs=('logs/app.log', 'a')"

    with patch("builtins.open", mock_open(read_data=original_config)) as mock_file:
        update_logging_config()
        mock_file.assert_called_with('logging.conf', 'w')
        mock_file().write.assert_called_once_with(expected_config)
