import unittest

import pytest

from core.entities import App


class Other_tests(unittest.TestCase):
    """
    For other negative, not in class methods (functions)
    """

    def test_should_not_create_unknown_agent_thought_fabric(self, config):
        with pytest.raises(NotImplementedError) as excinfo:
            App.agent_create(vendor_name='unknown_agent', config_ptr=config)

        assert "must be non-negative" in str(excinfo.value)