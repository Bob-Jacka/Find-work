"""
Main agent to use, because hh is the major
"""

from core.entities.Agents.IAgent import IAgent
from core.entities.Page_objects import Page_objects


class HH_agent(IAgent):

    def __init__(self, config):
        self.agent_name = 'HH agent'
        self.config_ptr = config
        self.favourite = list()
        self.later_see = list()

    def login(self) -> None:
        """
        Login page actions pipeline
        """
        self.browser, self.page = self.open_browser(self.config_ptr.vacancy_sites['hh'])
        self.config_ptr.browsers.append(self.browser)
        login_page = Page_objects.Login_page()
        login_page.add_element('login_field', '')
        login_page.add_element('password_field', '')
        login_page.add_behaviour('authenticate', lambda: None)

        self.vacancy()
        # Go to vacancy page

    def vacancy(self):
        """
        Vacancy page actions pipeline
        """
        Page_objects.proceed_to_page(self.page, '')
        vacancy_page = Page_objects.Vacancy_page()

    def search(self) -> None:
        # For vacancy page only
        print(f'{self.agent_name} started working at {IAgent.current_time()}')
        # search logic:
        self.login()

        print(f'{self.agent_name} ended working at {IAgent.current_time()}')

    def add_to_later(self) -> None:
        pass

    def add_to_possible(self) -> None:
        pass

    def apply_to_vacancy(self) -> None:
        pass
