"""
Main agent to use, because hh is the major
"""

from core.entities.Agents.IAgent import IAgent


class Page_objects:
    class _Login_page:
        telephone_field: str
        sign_in_btn: str

        def __init__(self, page):
            pass

    class _Vacancy_page:
        def __init__(self, page):
            pass


class HH_agent(IAgent):

    def __init__(self, config):
        self.agent_name = 'HH agent'
        self.config_ptr = config
        self.favourite = list()
        self.later_see = list()

    def login(self) -> None:
        browser, page = self.open_browser(self.config_ptr.vacancy_sites['hh'])
        self.config_ptr.browsers.append(browser)

        login_page = Page_objects._Login_page(page)

    def search(self) -> None:
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
