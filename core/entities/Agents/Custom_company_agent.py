"""
Class for custom company sites, for example, company has their own vacancies on their site and on aggregation sites
"""

from playwright.sync_api import Browser, Page

from core.entities.Agents.IAgent import IAgent


class Custom_company_agent(IAgent):
    company_name: str

    def __init__(self, config, company_name):
        self.agent_name = company_name
        self.company_name = company_name
        self.config_ptr = config
        self.favourite = list()
        self.later_see = list()

    def login(self) -> None:
        pass

    def search(self) -> None:
        pass

    def add_to_later(self) -> None:
        pass

    def add_to_possible(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass

    @staticmethod
    def open_browser(start_link: str) -> tuple[Browser, Page] | None:
        return super().open_browser(start_link)
