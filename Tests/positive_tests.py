import unittest

from core.entities import App
from core.entities.Agents.Custom_company_agent import Custom_company_agent
from core.entities.Agents.HH_agent import HH_agent
from core.entities.Agents.Habr_agent import Habr_agent
from core.entities.Agents.Max_agent import Max_agent
from core.entities.Agents.Rabotaru_agent import Rabotaru_agent
from core.entities.Agents.Superjob_agent import Superjob_agent
from core.entities.Agents.Telegram_agent import Telegram_agent


class Other_tests(unittest.TestCase):
    """
    For other, not in class methods (functions)
    """

    def test_should_create_agent_thought_fabric(self, config):
        hh_agent = App.agent_create(vendor_name='hh', config_ptr=config)
        assert hh_agent is not None


class Agents_create(unittest.TestCase):

    def test_should_create_hh_agent(self, config):
        agent = HH_agent(config)
        assert agent is not None

    def test_should_create_habr_agent(self, config):
        agent = Habr_agent(config)
        assert agent is not None

    def test_should_create_telegram_agent(self, config):
        agent = Telegram_agent(config)
        assert agent is not None

    def test_should_create_custom_company_agent(self, config):
        agent = Custom_company_agent(config, 'some company')
        assert agent is not None

    def test_should_create_max_agent(self, config):
        agent = Max_agent(config)
        assert agent is not None

    def test_should_create_superjob_agent(self, config):
        agent = Superjob_agent(config)
        assert agent is not None

    def test_should_create_rabotaru_agent(self, config):
        agent = Rabotaru_agent(config)
        assert agent is not None


class Agents_search(unittest.TestCase):
    pass


class Profile(unittest.TestCase):
    pass
