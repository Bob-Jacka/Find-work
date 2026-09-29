"""
Warning, might be error because telegram is forbidden
"""

from playwright.sync_api import Browser, Page

from core.entities.Agents.IAgent import IAgent


class Telegram_agent(IAgent):

    def __init__(self, config):
        self.agent_name = 'Telegram agent'
        self.config_ptr = config
        self.favourite = list()
        self.later_see = list()

    def login(self) -> None:
        pass

    def search(self) -> None:
        pass

    def add_to_later(self) -> None:
        pass

    def add_to_interesting(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass

    @staticmethod
    def open_browser(start_link: str) -> tuple[Browser, Page] | None:
        return super().open_browser(start_link)
